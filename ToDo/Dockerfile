# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install pipenv or other package manager if needed (optional)
RUN pip install --upgrade pip

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies from requirements.txt or Pipfile
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy your environment file
COPY .env /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Ensure gunicorn is installed
RUN pip install gunicorn

# Expose port 8000 for the web server
EXPOSE 8000

# Run the Django application with Gunicorn (you can configure number of workers)
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "ToDo.wsgi:application"]
