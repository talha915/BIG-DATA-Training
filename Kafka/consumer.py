from kafka import KafkaConsumer

# Kafka broker details
bootstrap_servers = 'localhost:9092'
topic = 'test_topic'

# Create a Kafka consumer
consumer = KafkaConsumer(
    topic,
    bootstrap_servers=bootstrap_servers,
    auto_offset_reset='earliest',
    group_id='my-group'
)

# Subscribe to the topic
consumer.subscribe([topic])
print(f"Subscribed to topic: {topic}")

# Consume messages
try:
    for message in consumer:
        print(f"Received message: {message.value.decode()}")
except KeyboardInterrupt:
    # Handle Ctrl+C gracefully
    print("Consumer interrupted")

# Close the consumer
consumer.close()
