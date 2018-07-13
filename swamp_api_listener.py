import RPi.GPIO as GPIO
import time, requests, json

lightState=0

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)


def getAPIState():
    global lightState
    url = "http://localhost/api/index.php"
    querystring = {"action":"get"}
    headers = {}
    response = requests.request("GET", url, headers=headers, params=querystring)
    print response.text
    lightState = int(json.loads(response.text)['status'])
    print lightState
#    changelightState()
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

def getlightState():
    return lightState

GPIO.output(16,GPIO.HIGH)


while True:
    getAPIState()
    time.sleep(3)
#while True:
#    input_state = GPIO.input(23)
#    getAPIState()
#    if input_state == False:
#        print('Button Pressed')
#	changelightState()
#	GPIO.output(18,GPIO.HIGH)
#	GPIO.output(17,GPIO.HIGH)

#	if getlightState() == 1:
#	    GPIO.output(17,GPIO.HIGH)
#	    GPIO.output(18,GPIO.LOW)
#	else:
#	    GPIO.output(18,GPIO.HIGH)
#	    GPIO.output(17,GPIO.LOW)
#
#	time.sleep(1)
#    else:
	
#	GPIO.output(18,GPIO.LOW)
#	GPIO.output(17,GPIO.LOW)
