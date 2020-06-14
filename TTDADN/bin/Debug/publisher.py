import paho.mqtt.client as mqtt
import argparse

# Parser
parser = argparse.ArgumentParser(description='Publisher')
parser.add_argument("--name", help="Name of client", default="Loliology_pub")
parser.add_argument("--broker", help="Broker address", default="13.76.87.87")
parser.add_argument("--port", help="Port", default=1883)
parser.add_argument("--topic", help="Topic to publish [Required]", required=True)
parser.add_argument("--state", help="State of light [Required]", required=True)
args = vars(parser.parse_args())

# Vars
name = args['name']
broker = args['broker']
port = args['port']
topic = args['topic']
state = args['state']

# Get json payload
payload = "{\"device_id\": \"d8_1\",\n\"value\": [\"" + str(state) + "\"]\n}"
print(payload)

# main
client = mqtt.Client(name)
client.connect(broker, port)
client.publish(topic, name + ": " + payload)