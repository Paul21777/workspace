

#!/bin/bash

# Build the Docker image
echo "Building Docker image..."
docker build -t apex-dashboard .

# Run the Docker container
echo "Running Docker container..."
docker run -p 5001:5001 apex-dashboard

