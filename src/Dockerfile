FROM python:3.9-slim

WORKDIR /app

# Install runtime deps first (better layer caching)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Tell Kubernetes which port the app uses
EXPOSE 8080

# Run the app
CMD ["python", "app.py"]
