#!/usr/bin/python
# Swamp IoT Button Service
# Ron Egli / Github.com/SmugZombie
# Simple script to listen for a button imput to update an api and activate LEDS
# Version 1.1

import RPi.GPIO as GPIO
import time, requests, json, logging, thread

# Define Global Variables
lightState=0

# Setup GPIO for our uses
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT) # Red LED
GPIO.setup(17,GPIO.OUT) # Green LED
GPIO.setup(16,GPIO.OUT) # Yellow LED

# Light Up Yellow to signify "ON"
GPIO.output(16,GPIO.HIGH)

# Setup Logger
logging.basicConfig(filename='runtime.log',level=logging.DEBUG)

# Retrieves the current status from the api and sets the light that color
def getAPIState():
    global lightState
    url = "http://localhost/api/index.php"
    querystring = {"action":"get"}
    headers = {}
    response = requests.request("GET", url, headers=headers, params=querystring)
#    print response.text
    lightState = int(json.loads(response.text)['status'])
    logging.debug(lightState)
    toggleLights()

# Toggles the color of the light
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

# Toggles the status of the light after accepting button input via the API
def toggleStatus():
    global lightState
    url = "http://localhost/api/index.php"
    querystring = {"action":"toggle"}
    headers = {}
    response = requests.request("GET", url, headers=headers, params=querystring)
    logging.debug(response.text)
    lightState = int(json.loads(response.text)['status'])

# Service to check the API at given interval, Recommended no faster than 1 second
def runAPIChecker(thread_name):
    logging.debug("Starting API Checker")
    try:
        while True:
            getAPIState()
            time.sleep(1)
    except:
        GPIO.cleanup()
        logging.debug("Killing API Checker")

# Service to check if the button is being pressed. Recommended no faster than 0.1 seconds
def runButtonListener(thread_name):
    logging.debug("Starting Button Listener")

    try:
        while True:
            input_state = GPIO.input(23)
            if input_state == False:
                logging.debug('Button Pressed')
                toggleStatus()
                time.sleep(2.5)
            time.sleep(0.1)
    except:
        GPIO.cleanup()
        logging.debug("Killing Button Listener")

# Handles the magic of threading
try:
   thread.start_new_thread( runAPIChecker, ("Thread-1", ) )
   thread.start_new_thread( runButtonListener, ("Thread-2", ) )
except:
   print "Error: unable to start thread"

while 1:
   pass