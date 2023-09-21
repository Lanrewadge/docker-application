# Use a base image with Python installed
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the application files into the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port your application is running on
EXPOSE 5000

# Define the command to run your application
CMD ["python", "app.py"]
