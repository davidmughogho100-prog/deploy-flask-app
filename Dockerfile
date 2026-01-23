# Use a valid, modern slim Python base image 
FROM python:3.12-slim

# Set the working directory inside the container 
WORKDIR /usr/src/app

# Install OpenJDK 17 JRE 
RUN apt-get update && \
    apt-get install -y java && \
    apt-get clean;

# Install Python requirements [cite: 2]
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code [cite: 2]
COPY . .

# Set environment variables for Java 
ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-amd64/
ENV PATH $JAVA_HOME/bin:$PATH

# Expose the port 

# Corrected Command to run your Flask application 
CMD ["gunicorn", "-b", "0.0.0.0:$PORT", "main:app"]
