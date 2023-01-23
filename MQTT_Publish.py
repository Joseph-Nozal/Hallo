import paho.mqtt.client as mqtt
import json

host = 'test.mosquitto.org'
port = 1883
group = 'calculus2'
yourname = 'Joseph'
topic = group + '/' + yourname
username = ' '
password = ' '

client = mqtt.Client()
client.username_pw_set(username, password)
client.connect(host, port)

data = {}
data['name'] = 'Joseph Miles Nozal'
data['nickname'] = 'Joseph'
data['age'] = 20
data['occupation'] = 'Student'
data['FOE'] = 'Touched Grass'
data['com-lang'] = ['Java, Python']
data['table'] = 0
print('Original Input Data Type : {}'.format(type(data)))

data = json.dumps(data)
print ('Converted Input Data Type: {}'.format(type(data)))

try:
        client.publish(topic = topic, payload = data, qos = 0, retain = True)
        print ('Publish Success')

except:
        print ('Publish Fail') 

print ('Hotdog')