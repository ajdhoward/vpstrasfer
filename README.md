# AI Gateway Stack

This is the full stack to run an AI task orchestration system including:
- Redis-backed job queue
- FastAPI gateway
- Docker-based agent workers
- Plugin discovery from HuggingFace, GitHub, and more

Run:

```bash
docker compose up --build -d
```

📡 Gateway available at: http://localhost:8800  
🧠 Add your AI logic in: `agent_worker/main.py`
