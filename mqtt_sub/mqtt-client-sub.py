import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))

mqttBroker ="192.168.0.100"

client = mqtt.Client("Smartphone")
client.connect(mqttBroker, 11885) 

client.loop_start()

client.subscribe("new topic")
client.on_message=on_message 

time.sleep(30)
