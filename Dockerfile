# Use official Python runtime as a parent image
FROM python:3.12-slim

# Install build dependencies for mysqlclient
RUN apt-get update && apt-get install -y \
    pkg-config \    
    build-essential \
    libmariadb-dev-compat \ 
    libmariadb-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Django will run on
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
