FROM python:3.9-slim
RUN pip install redis
COPY main.py /app/main.py
WORKDIR /app
CMD ["python", "main.py"]
