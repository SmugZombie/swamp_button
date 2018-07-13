#!/usr/bin/python
import thread
import RPi.GPIO as GPIO
import time, requests, json, logging

lightState=0
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT) # Red LED
GPIO.setup(17,GPIO.OUT) # Green LED
GPIO.setup(16,GPIO.OUT) # Yellow LED

# Light Up Yellow
GPIO.output(16,GPIO.HIGH)

logging.basicConfig(filename='runtime.log',level=logging.DEBUG)

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

def runAPIChecker(thread_name):
    logging.debug("Starting API Checker")
    try:
        while True:
            getAPIState()
            time.sleep(1)
    except:
        GPIO.cleanup()
        logging.debug("Killing API Checker")
    #    GPIO.output(18,GPIO.LOW)
    #    GPIO.output(17,GPIO.LOW)
    #    GPIO.output(16,GPIO.HIGH)


def runButtonListener(thread_name):
    logging.debug("Starting Button Listener")
    def toggleStatus():
        global lightState
        url = "http://localhost/api/index.php"
        querystring = {"action":"toggle"}
        headers = {}
        response = requests.request("GET", url, headers=headers, params=querystring)
        logging.debug(response.text)
        lightState = int(json.loads(response.text)['status'])

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

# Create two threads as follows
try:
   thread.start_new_thread( runAPIChecker, ("Thread-1", ) )
   thread.start_new_thread( runButtonListener, ("Thread-2", ) )
   #thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print "Error: unable to start thread"

while 1:
   pass