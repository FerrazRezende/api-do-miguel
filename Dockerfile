# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory to /app
WORKDIR .

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r /app/app/requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable for the host and port
ENV HOST=0.0.0.0
ENV PORT=80

# Run main.py when the container launches
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
