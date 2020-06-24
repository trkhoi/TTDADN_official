import paho.mqtt.client as mqtt
import argparse

# Parser
parser = argparse.ArgumentParser(description='Publisher')
parser.add_argument("--name", help="Name of client", default="Loliology_pub")
parser.add_argument("--broker", help="Broker address", default="52.163.84.252")
parser.add_argument("--port", help="Port", default=1883)
parser.add_argument("--topic", help="Topic to publish", default="Topic/LightD")
parser.add_argument("--on", help="Light ON/OFF [Required]", required=True)
parser.add_argument("--bright", help="Light brightness [Required]", required=True)
args = vars(parser.parse_args())

# Vars
name = args['name']
broker = args['broker']
port = args['port']
topic = args['topic']
on = args['on']
bright = args['bright']

# Get json payload
payload = "{\"device_id\": \"Light_D\",\"value\": [\""+str(on)+"\", \""+str(bright)+"\"]}"
print(payload)

# main
client = mqtt.Client(name)
client.connect(broker, port)
client.publish(topic, name + ": " + payload)