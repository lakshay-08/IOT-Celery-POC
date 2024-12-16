import paho.mqtt.client as mqtt
import random
import time
import json

BROKER = "mqtt-broker"
PORT = 1883
TOPIC = "sensor/data"

client = mqtt.Client()

client.connect(BROKER, PORT, 60)

def publish_sensor_data():
    while True:
        data = {
            "sensor_id": random.randint(1, 10),
            "variable_1": round(random.uniform(20.0, 30.0), 2),
            "variable_2": round(random.uniform(-70.0, 70.0), 2),
            "variable_3": round(random.uniform(0.0, 70.0), 2),
            "variable_4": round(random.uniform(0.0, 70.0), 2),
            "variable_5": round(random.uniform(0.0, 70.0), 2),
            "variable_6": round(random.uniform(0.0, 70.0), 2),
            "variable_7": round(random.uniform(0.0, 700.0), 2),
            "variable_8": round(random.uniform(-30.0, 70000.0), 2),
        }
        client.publish(TOPIC, json.dumps(data))
        print(f"Published: {data}")
        time.sleep(2)

if __name__ == "__main__":
    publish_sensor_data()
