import network
import socket
import time

from machine import Pin

ssid = 'PUBLIC_SSID'
password = 'IDK'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

reed_sw = Pin(16, Pin.IN)



# Check flash for the following info - SSID/Password, MQTT
# Server/ClientID/Pswd/Topic
# If not - start a hotspot with SSID = garage_iot / password = garage_iot
#   Serve up page that allows them to setup required info
#   Save to flash
#   Reboot

# If so - connect to wifi
#  If wifi connect fails, delete from flash and reboot
#  If wifi connect succeeds, connect to MQTT server
#    if mqtt connect fails, delete from flash and reboot
#    if mqtt connect succeeds, transmit

# Main event loop
#   Setup Watchdog Timer
#   Setup pin 16 as input
#   Setup pin 16 as interrupt
#   Setup a 15 min timer as interrupt
#   Add initial status into event queue
#   Enter event queue wait and server ping
#      write timestamp to topic/health
#      While event.len > 0: 
#         write to topic on mqtt server
#      sleep waiting for interrupt

# Reed Interrupt
#   Wait 100ms for bounce to settle
#   Read pin 16 status
#   Add status and time to event queue

# Time Interrupt
# Exit to main loop

