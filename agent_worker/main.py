import redis
import json

r = redis.Redis(host='redis', port=6379)
print("🤖 Worker running...")
while True:
    task = r.blpop('tasks')
    if task:
        job = json.loads(task[1])
        print(f"🛠️ Processing task: {job['type']}")
        # Add processing logic here
