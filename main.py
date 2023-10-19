from fastapi import FastAPI
import prometheus_client
from tortoise.contrib.fastapi import register_tortoise
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

from fastapi import Response

app = FastAPI(title='Alam Store')


heads_count = Counter("home_requests", "Some description")


@app.get("/home")
async def hello():
    heads_count.inc()
    return {"Hello":"World"}


@app.get("/metrics")
async def metrics():
    return Response(
        media_type="text/plain",
        content=prometheus_client.generate_latest(),
    )