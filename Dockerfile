FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ ./src/
COPY models/ ./models/
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]