# Use official python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for mkdocs server
EXPOSE 8000

# Run mkdocs serve when the container launches
CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]