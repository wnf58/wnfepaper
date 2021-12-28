#!/usr/bin/env python3

import json
import paho.mqtt.client as mqtt

BBB_IP = '192.168.80.106'
TOPIC = '/c2016/wnfPlay'


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # client.subscribe("computer/esp1")
    client.subscribe(TOPIC)


def on_message(client, userdata, msg):
    try:
        aJson = json.loads(msg.payload.decode('utf8'))
        print(aJson)
        # print(aJson['TEMP'])
    except Exception as E:
        print('Fehler', E)
        raise


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    z = client.connect(BBB_IP, 1883, 60)
    print(z)
    client.loop_forever()


if __name__ == '__main__':
    main()
