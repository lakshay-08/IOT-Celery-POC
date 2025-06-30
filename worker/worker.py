import paho.mqtt.client as mqtt
from tasks import process_sensor_data

BROKER = "mqtt-broker"
PORT = 1883
TOPIC = "sensor/data"

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    print(f"Received: {message}")
    process_sensor_data.delay(message)

client = mqtt.Client()
client.connect(BROKER, PORT, 60)
client.subscribe(TOPIC)
client.on_message = on_message

print("Worker listening to MQTT broker...")
client.loop_forever()
