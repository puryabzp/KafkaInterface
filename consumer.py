import json
from confluent_kafka import Consumer, KafkaError

class KafkaConsumer:
    def __init__(self, config_file):
        self.config = self.load_config(config_file)

    def load_config(self, config_file):
        try:
            with open(config_file, 'r') as file:
                config = json.load(file)
            return config
        except FileNotFoundError:
            print(f"Config file '{config_file}' not found.")
            exit(1)
        except json.JSONDecodeError:
            print(f"Invalid JSON format in config file '{config_file}'.")
            exit(1)

    def consume(self):
        consumer = Consumer({
            'bootstrap.servers': self.config.get('bootstrap_servers', 'localhost:9092'),
            'group.id': self.config.get('group_id', 'my_consumer_group'),
            'auto.offset.reset': 'earliest'
        })

        # Read topics from the configuration file
        topics = self.config.get('topics', ['inventory'])
        consumer.subscribe(topics)

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
    consumer = KafkaConsumer('config.json')  # Pass the config file path here
    consumer.run()
