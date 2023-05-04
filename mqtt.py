import paho.mqtt.client as mqtt

import time

MQTT_Broker = "10.45.42.130"
MQTT_Port = 1883
Keep_Alive_Interval = 3600
MQTT_Topic = "prod/#"

def on_connect(self, mosq, obj, rc):
	mqttc.subscribe(MQTT_Topic, 0)


def on_message(mosq, obj, msg):
	print("MQTT Data Received...")
	print("MQTT Topic: " + msg.topic)  
	print("Data: " + msg.payload)


def on_subscribe(mosq, obj, mid, granted_qos):
    pass
client_id = "test"
mqttc = mqtt.Client(client_id)
