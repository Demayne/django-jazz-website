# Use the official Python image.
FROM python:3.11-slim

# Set environment variables to prevent Python from writing .pyc files and buffering stdout/stderr.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory to /app.
WORKDIR /app

# Install system dependencies.
RUN apt-get update && \
    apt-get install -y build-essential libpq-dev dos2unix && \
    apt-get clean

# Copy the requirements.txt file into the /app directory.
COPY requirements.txt /app/

# Install the Python dependencies.
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the entire mySite project directory into the /app directory.
COPY mySite/ /app/

# Copy the entrypoint.sh script into the /app directory.
COPY entrypoint.sh /app/

# Convert entrypoint.sh to Unix format and add execute permissions.
RUN dos2unix /app/entrypoint.sh && \
    chmod +x /app/entrypoint.sh

# Collect static files
RUN python manage.py collectstatic --noinput

# Set PYTHONPATH to include /app
ENV PYTHONPATH=/app

# Set the Django settings module environment variable
ENV DJANGO_SETTINGS_MODULE=mySite.settings

# Expose the port the app runs on.
EXPOSE 8000

# Run the shell script when the container starts.
ENTRYPOINT ["/app/entrypoint.sh"]
