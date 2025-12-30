FROM python:3.11-slim
WORKDIR /app
COPY . /app
ENV MODEL_MODE=hosted
CMD ["python", "run.py"]
