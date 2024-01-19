# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port on which the FastAPI application will run
EXPOSE 8000

# Specify the command to run the application
CMD ["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8000"]
