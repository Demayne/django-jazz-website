# Use the official Python image as the base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY . /app/

# Ensure the entry point script is executable
RUN chmod +x /app/entrypoint.sh

# Expose the port that the application runs on
EXPOSE 8000

# Set the entry point for the container
ENTRYPOINT ["/app/entrypoint.sh"]
