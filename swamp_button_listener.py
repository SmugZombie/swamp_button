# Swamp AButton Listener
# Ron Egli / Github.com/SmugZombie
# Simple script to listen for a button imput to update an api
# Version 1.0

import RPi.GPIO as GPIO
import time, requests, json

lightState=1

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(False)

def toggleStatus():
    global lightState
    url = "http://localhost/api/index.php"
    querystring = {"action":"toggle"}
    headers = {}
    response = requests.request("GET", url, headers=headers, params=querystring)
    print response.text
    lightState = int(json.loads(response.text)['status'])

while True:
    input_state = GPIO.input(23)
    if input_state == False:
        print('Button Pressed')
	toggleStatus()
	time.sleep(1)
