from fastapi import FastAPI, Request
import redis
import json

app = FastAPI()
r = redis.Redis(host='redis', port=6379)

@app.post("/query")
async def route_query(req: Request):
    data = await req.json()
    r.rpush("tasks", json.dumps(data))
    return {"status": "queued", "task": data}

@app.get("/status")
def status():
    return {"status": "ok", "services": ["redis", "worker", "gateway"]}
