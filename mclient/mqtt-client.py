import paho.mqtt.client as mqtt 
import time

mqttBroker ="192.168.0.100" # Ip address

client = mqtt.Client("First Mqtt Message")
client.connect(mqttBroker, 11885) 

while True:
    client.publish("new topic", "My name is rifat") # publishing message to the specific topic
    print("Just published My name")
    time.sleep(1)
