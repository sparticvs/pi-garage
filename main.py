###
# Copyright 2022 Charles `sparticvs` Timko
###
import OPi.GPIO as GPIO
import paho.mqtt.client as mqtt

MQTT_HOST = "192.168.1.5"
MQTT_PORT = 1883
MQTT_CLIENT = "garage"
MQTT_PASS = "VMh29Dpbm2"
MQTT_TOPIC = "home/garage/state"

SENSOR = 12
BOUNCE = 200

def on_sensor_on():
    mqtt.publish(MQTT_TOPIC, payload=1)

def on_sensor_off():
    mqtt.publish(MQTT_TOPIC, payload=0)

## Setup MQTT Client
mqtt.connect(MQTT_HOST)
mqtt.loop_start()

## Setup GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

## Register Event Callbacks
GPIO.add_event_detect(
        SENSOR, GPIO.RISING,
        callback=on_sensor_on,
        bouncetime=BOUNCE)
GPIO.add_event_detect(
        SENSOR, GPIO.FALLING,
        callback=on_sensor_off,
        bouncetime=BOUNCE)

while True:
    pass

GPIO.cleanup()
