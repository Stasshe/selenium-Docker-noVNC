# Use the official Selenium standalone Chrome image as the base
FROM selenium/standalone-chrome

# Set environment variables
ENV SE_NODE_SESSION_TIMEOUT=3000
ENV SCREEN_WIDTH=1280
ENV SCREEN_HEIGHT=720
ENV SCREEN_DEPTH=24

# Expose ports
EXPOSE 4444
EXPOSE 7900

# Set shared memory size
VOLUME /dev/shm

# Run the container with the specified settings
CMD ["selenium-standalone", "start", "-debug"]
