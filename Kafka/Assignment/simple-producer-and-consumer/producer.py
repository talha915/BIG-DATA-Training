from kafka import KafkaProducer

#Brocker details

bootstrap_servers = 'localhost:9092'
topic = 'test_topic_1'

producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

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