FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY app.py .

# App listens on 8080
EXPOSE 8080
ENV PORT=8080

CMD ["python", "app.py"]
