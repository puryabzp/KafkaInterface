import json
from confluent_kafka import Producer


class KafkaProducer:
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

    def produce(self):
        producer = Producer({'bootstrap.servers': self.config.get('bootstrap_servers', 'localhost:9092')})
        while True:
            topic = input("Enter the topic (or 'exit' to quit): ")
            if topic == "exit":
                break
            key_value = input("Enter the key-value pair (e.g., '104,30') or just the value: ")

            if ',' in key_value:
                key, value = key_value.split(',')  # Split the input into key and value
                self.send_message(producer, topic, key, value)
            else:
                self.send_message(producer, topic, None, key_value)

    def send_message(self, producer, topic, key, value):
        message_key = key.encode('utf-8') if key else None
        producer.produce(topic=topic, key=message_key, value=value.encode('utf-8'))
        producer.flush()
        if key:
            print(f"Sent message with key: {key}, value: {value}")
        else:
            print(f"Sent message: {value}")

    def run(self):
        self.produce()


if __name__ == '__main__':
    producer = KafkaProducer('config.json')  # Pass the config file path here
    producer.run()
