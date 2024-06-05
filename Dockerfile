# Use the official Python image.
FROM python:3.11-slim

# Set environment variables to prevent Python from writing .pyc files and buffering stdout/stderr.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory to /app.
WORKDIR /app

# Install system dependencies.
RUN apt-get update && \
    apt-get install -y build-essential libpq-dev && \
    apt-get clean

# Copy the requirements.txt file into the /app directory.
COPY requirements.txt /app/

# Install the Python dependencies.
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the entire mysite project directory into the /app directory.
COPY mySite /app/mySite

# Copy the manage.py file into the /app directory.
COPY mySite/manage.py /app/

# Copy the entrypoint.sh script into the /app directory.
COPY entrypoint.sh /app/

# Convert entrypoint.sh to Unix format and add execute permissions.
RUN apt-get install -y dos2unix && \
    dos2unix /app/entrypoint.sh && \
    chmod +x /app/entrypoint.sh

# Expose the port the app runs on.
EXPOSE 8000

# Run the shell script when the container starts.
ENTRYPOINT ["/app/entrypoint.sh"]
