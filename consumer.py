from confluent_kafka import Consumer, KafkaError


class KafkaConsumer:
    def __init__(self):
        self.bootstrap_servers = 'localhost:9092'
        self.group_id = 'my_consumer_group'

    def consume(self):
        consumer = Consumer({
            'bootstrap.servers': self.bootstrap_servers,
            'group.id': self.group_id,
            'auto.offset.reset': 'earliest'
        })
        consumer.subscribe(['your-topics'])  # Add your desired topics here

        while True:
            message = consumer.poll(1.0)
            if message is None:
                continue
            if message.error():
                if message.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(f"Consumer error: {message.error()}")
                    break

            print(f"Received message on topic '{message.topic()}' with value: {message.value().decode()}")

    def run(self):
        self.consume()


if __name__ == '__main__':
    consumer = KafkaConsumer()
    consumer.run()
