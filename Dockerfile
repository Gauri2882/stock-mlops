FROM python:3.13-slim
WORKDIR /app

# Install pipenv
RUN pip install pipenv

# Copy Pipfiles
COPY Pipfile Pipfile.lock ./

# Install dependencies
RUN pipenv install --system --deploy

# Copy app files
COPY src/ ./src/
COPY models/ ./models/

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]