# Use a lightweight base image with Python
FROM python:3.9-slim

# Set PySpark and Hadoop versions
ENV PYSPARK_VERSION=3.5.1
ENV HADOOP_VERSION=3

# Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    openjdk-17-jdk-headless \
    wget \
    ca-certificates \
    gnupg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install PySpark
RUN wget https://archive.apache.org/dist/spark/spark-${PYSPARK_VERSION}/spark-${PYSPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \
    tar -xzf spark-${PYSPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \
    mv spark-${PYSPARK_VERSION}-bin-hadoop${HADOOP_VERSION} /usr/local/spark && \
    rm spark-${PYSPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz

# Set environment variables for Spark
ENV SPARK_HOME=/usr/local/spark
ENV PATH=$PATH:$SPARK_HOME/bin
ENV PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.9-src.zip

# Set a working directory
WORKDIR /app

# Copy the requirements file into the container
COPY ../../requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install -r /app/requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Command to keep the container running
CMD ["tail", "-f", "/dev/null"]
