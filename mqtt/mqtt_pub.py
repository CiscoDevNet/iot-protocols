import paho.mqtt.client as mqtt


broker_ip = 'broker.hivemq.com'
broker_port = 1883
mqtt_topic = 'devnetzone/topic'
payload = '{"message":"Hello World"}'

def on_connect(mqttc, obj, flags, rc):
    print("connected")


def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))
    pass

def mqtt_pub(payload): #function to publish payload to a topic
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.connect(broker_ip, broker_port, 60)
    client.publish(mqtt_topic, payload)
    print('MESSAGE PUB [x] ' + payload)
    client.disconnect()


if __name__ == '__main__':
    mqtt_pub(payload)
