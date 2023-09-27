from confluent_kafka import Producer


class KafkaProducer:
    def __init__(self):
        self.bootstrap_servers = 'localhost:9092'

    def produce(self):
        producer = Producer({'bootstrap.servers': self.bootstrap_servers})
        while True:
            topic = input("Enter the topic (or 'exit' to quit): ")
            if topic == "exit":
                break
            message = input("Enter the message: ")
            self.send_message(producer, topic, message)

    def send_message(self, producer, topic, message):
        producer.produce(topic=topic, value=message)
        producer.flush()
        print(f"Sent message: {message}")

    def run(self):
        self.produce()


if __name__ == '__main__':
    producer = KafkaProducer()
    producer.run()
