FROM python:3.11-slim

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the bot code
COPY . .

# Create logs directory and set permissions before switching user
RUN mkdir -p /app/logs && \
    chmod 777 /app/logs

# Create a non-root user for security
RUN useradd -m botuser
USER botuser

# Run the bot
CMD ["python", "main.py"]