# Use the official Python image as a base
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Install Flask and other dependencies
RUN pip install Flask lxml

# Copy the rest of the application code to the working directory
COPY . .

# Expose port 5000 to the outside world
EXPOSE 5000

# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0"]
