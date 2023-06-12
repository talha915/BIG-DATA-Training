from kafka import KafkaProducer

# Kafka broker details
bootstrap_servers = 'localhost:9092'
topic = 'test_topic'

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# Produce messages
messages = [
    b'Ho 1',
    b'Hi 2',
    b'HoHI 3'
]

for message in messages:
    print(topic, message)
    producer.send(topic, message)

# Flush and close the producer
producer.flush()
producer.close()
