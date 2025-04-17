FROM python:3.13-slim  

WORKDIR /app

# Install pipenv first
RUN pip install --no-cache-dir pipenv

# Copy only Pipfiles first (for layer caching)
COPY Pipfile Pipfile.lock ./

# Install dependencies
RUN pipenv install --system --deploy

# Copy application
COPY src/ ./src/
COPY models/ ./models/

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]