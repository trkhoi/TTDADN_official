import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import argparse
import json
import time
from mongodb_database import MyDatabase
# Parser
parser = argparse.ArgumentParser(description='Subscriber')
parser.add_argument("--name", help="Name of client", default="Backend")
parser.add_argument("--broker", help="Broker address", default="52.163.84.252")
parser.add_argument("--port", help="Port", default=1883)
parser.add_argument("--topic", help="Topic to subscribe to [Required]", default="tft")
args = vars(parser.parse_args())

# Vars
name = args['name']
broker = args['broker']
port = args['port']
topic = args['topic']

### Database
mydb = MyDatabase()

# on_message function
def on_message(client, userdata, message):
    data = str(message.payload.decode("utf-8"))
    data=json.loads(data)
    print(data)
    t = time.localtime(time.time())
    name_txt = data["device_id"] + "_" + str(t.tm_min) + "_" + str(t.tm_hour)
    f = open(name_txt + ".txt",'w')
    if data["device_id"] == "TempHumi":
        print(data["device_id"],data["values"][0],data["values"][1])
        f.write(data["device_id"] + "," + data["values"][0] + "," + data["values"][1] + "\n")
        mydb.insert_temp_humid(int(data["values"][0]),int(data["values"][1]))
    elif data["device_id"] == "Light":
        print(data["device_id"],data["values"][0])
        f.write(data["device_id"] + "," + data["values"][0] + "\n")
        mydb.insert_light(int(data["values"][0]))
    else:
        pass
    print("finish")
    f.close()

subscribe.callback(on_message, ["Topic/Light","Topic/TempHumi"], hostname=broker)
# main
# client = mqtt.Client(name)
# client.on_message = on_message
# client.connect(broker, port)
# client.subscribe(topic)
# client.loop_forever()