# Use a lightweight base image
FROM python:3.9-slim

# Set environment variables
ENV PYSPARK_VERSION=3.1.2
ENV HADOOP_VERSION=3.2

# Install dependencies
RUN apt-get update && \
    apt-get install -y openjdk-11-jre-headless && \
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

# Install Jupyter
RUN pip install --no-cache-dir jupyter

# Install PySpark
RUN pip install --no-cache-dir pyspark==${PYSPARK_VERSION}

# Set up Jupyter configuration
RUN jupyter notebook --generate-config
COPY jupyter_notebook_config.py /root/.jupyter/

# Expose Jupyter port
EXPOSE 8888

# Start Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]