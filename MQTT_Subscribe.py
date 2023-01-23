import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import json

host = 'test.mosquitto.org'
port = 1883
group = 'calculus2'
yourname = 'Joseph'
topic = group + '/' + yourname
username = ''
password = ''

client = mqtt.Client()
client.username_pw_set(username, password)
client.connect(host, port)

try:
        msg = subscribe.simple(topic, hostname = host, port = port)
        print ('Subscribe Success')
        get_topic = msg.topic
        data = msg.payload
        print ('{} : {}'.format(get_topic, data))
        print ('Recieved Data Type: {}'.format(type(data)))
        data = json.loads(data)
        print ('Converted Data : {}'.format(data))
        print ('Converted Data Type: {}'.format(type(data)))
        
except:
        print ('Subscribe Fail') 