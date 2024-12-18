# Use Python 3.10 with Debian Bullseye
FROM python:3.10-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to install dependencies
COPY requirements.txt requirements.txt

# Install dependencies and SQLite
RUN apt-get update && apt-get install -y sqlite3

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files to the container
COPY . .

# Set environment variables for Django
ENV PYTHONDONTWRITEBYTECODE 1  # Avoids .pyc files
ENV PYTHONUNBUFFERED 1         # Ensures logs are streamed directly

# Expose the port the app runs on
EXPOSE 8000

# Run Django migrations and start the development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
