# Use Python 3.10.11 image as the base
FROM python:3.10-slim-bullseye

# Set the working directory
WORKDIR /app

# Copy the current directory to the container 
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000  
EXPOSE 8000

# Start mkdocs dev server
CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]