# Use the official Python image from the Docker Hub
FROM python:3.10-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any dependencies
RUN pip install --upgrade pip \
    && pip install setuptools wheel\
    && pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /app/

# Expose the port that FastAPI will run on
EXPOSE 8000

# Copy the entrypoint script
COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

# Command to run the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
