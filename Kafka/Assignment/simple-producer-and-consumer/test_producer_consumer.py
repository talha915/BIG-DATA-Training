from kafka import KafkaProducer
from kafka import KafkaConsumer
import pytest

# Test case for verifying if messages are produced successfully
def test_producer():
    # Define the Kafka broker details
    bootstrap_servers = 'localhost:9092'
    topic = 'test_topic_assert'

    # Create a Kafka producer
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

    # Produce a test message
    message = b'Test Message'
    producer.send(topic, message)
    producer.flush()
    producer.close()

    # Create a Kafka consumer
    consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_servers)
    
    # Consume messages
    for msg in consumer:
        print(msg, message)
        assert msg.value == message
        break  # Break after consuming the first message

    consumer.close()

# Run the tests
if __name__ == '__main__':
    test_producer()
