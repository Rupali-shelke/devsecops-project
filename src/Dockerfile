# Use Python 3.9 as base image
FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy all files from current directory (src) to /app
COPY . .

# Install dependencies if you have any (create requirements.txt if needed)
# RUN pip install --no-cache-dir -r requirements.txt

# Default command to run the app
CMD ["python", "app.py"]
