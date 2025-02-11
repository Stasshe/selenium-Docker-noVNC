# Use the official Selenium standalone image as the base
FROM selenium/standalone-chrome

# Set environment variables
ENV SE_VNC_PASSWORD=mypass

# Install Python and necessary dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

# Copy the requirements file
COPY requirements.txt /app/requirements.txt

# Install Python packages
RUN pip3 install -r /app/requirements.txt

# Copy the Selenium script
COPY selenium_test.py /app/selenium_test.py

# Set the working directory
WORKDIR /app

# Run the Selenium script
CMD ["python3", "/app/selenium_test.py"]
