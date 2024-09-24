# Step 1: Use an official Python runtime as a base image
FROM python:3.9-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Step 4: Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the application code to the container
COPY . /app

# Step 6: Set the environment variable for Flask
ENV FLASK_APP=core/server.py

# Step 7: Expose the port on which the Flask app runs
EXPOSE 5000

# Step 8: Command to run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
