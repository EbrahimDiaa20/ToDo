# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the Django app runs
EXPOSE 8000

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=ToDo.settings
ENV PYTHONUNBUFFERED 1

# Run migrations and start Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
