# Swamp API Listener
# Ron Egli / Github.com/SmugZombie
# Simple script to check an API status and relay via LEDS
# Version 1.0

import RPi.GPIO as GPIO
import time, requests, json

lightState=0
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT) # Red LED
GPIO.setup(17,GPIO.OUT) # Green LED
GPIO.setup(16,GPIO.OUT) # Yellow LED

def getAPIState():
    global lightState
    url = "http://localhost/api/index.php"
    querystring = {"action":"get"}
    headers = {}
    response = requests.request("GET", url, headers=headers, params=querystring)
    print response.text
    lightState = int(json.loads(response.text)['status'])
    print lightState
    toggleLights()

def toggleLights():
    global lightState
    if lightState == 1:
	# red
        GPIO.output(18,GPIO.HIGH)
        GPIO.output(17,GPIO.LOW)
    else:
	# green
        GPIO.output(17,GPIO.HIGH)
        GPIO.output(18,GPIO.LOW)

# Light Up Yellow
GPIO.output(16,GPIO.HIGH)

while True:
    getAPIState()
    time.sleep(3)
