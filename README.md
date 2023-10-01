# Docker Setup for Kafka and Zookeeper And Kafka Interface

This Docker Compose configuration file (`docker-compose.yaml`) sets up Kafka and Zookeeper services using Confluent's official Docker images. It also includes Python scripts (`producer.py` and `consumer.py`) for producing and consuming messages from Kafka topics. Below, you'll find instructions on how to set up and use this environment.

## Prerequisites

1. Docker: Ensure you have Docker installed on your system.

## Setup
1. Clone the project repository from GitHub:

   ```bash
   git clone https://github.com/puryabzp/KafkaInterface.git
   ```
   Navigate to the project directory:
   ```bash
   cd KafkaInterface
   ```
   Run:
   ```bash
   pipenv shell
   ```
   Then:
   ```bash
   (KafkaInterface) youruser@youruser:~/yourdirectory/KafkaInterface$ pipenv install 
   ```


## Running the Kafka and Zookeeper Services

1. Open your terminal and navigate to the directory containing the `docker-compose.yaml` file.

2. Run the following command to start the Kafka and Zookeeper services:

   ```bash
   docker-compose up -d
   ```

   This will launch Kafka and Zookeeper containers in the background.

## Accessing the Kafka Container Bash

You can access the Kafka container's bash shell to interact with Kafka using command-line tools.

1. Find the name of the Kafka container:

   ```bash
   docker ps -a
   ```

   Look for the container with the name starting with `yourproject_kafka_`.

2. Access the Kafka container's bash shell:

   ```bash
   docker-compose exec -it kafka /bin/bash
   ```
3. for Creating the Kafka topic test_topic with 3 partitions and a replication factor of 1 when my Kafka broker is running at localhost:9092

   ```bash
   kafka-topics --bootstrap-server localhost:9092 --topic test_topic --create --partitions 3 --replication-factor 1
   ```
4. To list Kafka topics, we need to provide the mandatory parameters:
   ```bash
   kafka-topics --bootstrap-server localhost:9092 --list
   ```
5. To produce to a Kafka topic:
   ```bash
      kafka-console-producer --bootstrap-server localhost:9092 --topic test_topic
   ```
   command output:   
      ```bash
     >
      ```
   then you can write your own message:
      ```bash
      >Hello World
      >^C  (<- Ctrl + C is used to exit the producer)
      ```
6. for Consume only the future messages of a Kafka topic:
   ```bash
      kafka-console-consumer --bootstrap-server localhost:9092 --topic test_topic
   ```
   Consume all historical messages and future ones in a Kafka topic:
   ```bash
      kafka-console-consumer --bootstrap-server localhost:9092 --topic test_topic --from-beginning
   ```
7. To change the size-based retention for a topic, you can use the kafka-configs tool as follows:
   ```bash
      kafka-configs --bootstrap-server localhost:9092 --alter --entity-type topics --entity-name <TOPIC_NAME> --add-config retention.ms=<NEW_RETENTION_TIME_IN_MILLISECONDS>
   ```
## Producing Messages

To produce messages to a Kafka topic, use the `producer.py` script. Follow these steps:

1. Ensure you have Python installed on your local machine.

2. In a new terminal, navigate to the directory where you placed `producer.py`.

   3. Run the producer script:

      ```bash
      python producer.py
      ```

      You will be prompted to enter the topic and message you want to produce.
      ```bash
         # Produce a message to a Kafka topic using producer.py
         python producer.py

         # Example input:
         # Enter the topic (or 'exit' to quit): test-topic
         # Enter the message: Hello, Kafka!
      ```

## Consuming Messages

To consume messages from Kafka topics, use the `consumer.py` script. Follow these steps:

1. Ensure you have Python installed on your local machine.

2. In a new terminal, navigate to the directory where you placed `consumer.py`.

   3. Run the consumer script:

      ```bash
      python consumer.py
      ```

      This script subscribes to the topic(s) you specify in the `consumer.py` code and displays received messages.
      ```bash
       # Consume messages from a Kafka topic using consumer.py
       python consumer.py
   
       # Output (when a message is received):
       # Received message on topic 'test-topic' with value: Hello, Kafka!
   
       # To exit the consumer, press Ctrl+C.
      ```


Now you can use the provided Python scripts (`producer.py` and `consumer.py`) to produce and consume messages from Kafka topics within your Dockerized Kafka environment. Make sure to customize the topics and group IDs as needed in the scripts.

Feel free to replace `your-topics` in the `consumer.py` script with the actual Kafka topics you want to consume from.
