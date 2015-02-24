import RPi.GPIO as GPIO
import time

SOUND_CM_PER_SEC = 34000

trig = 16
echo = 11

def setup(trigger_pin, echo_pin):
	trig = trigger_pin
	echo = echo_pin

	GPIO.setup(trig, GPIO.OUT)
	GPIO.setup(echo, GPIO.IN)

	GPIO.output(trig, False)

	time.sleep(0.5)


def get_distance():
	GPIO.output(trig, True)
	time.sleep(0.00001)
	GPIO.output(trig, False)

	start = time.time()

	while GPIO.input(echo)==0:
		start = time.time()

	while GPIO.input(echo)==1:
		stop = time.time()

	elapsed = stop-start

	# Calculate distance
	distance = elapsed * SOUND_CM_PER_SEC

	return distance
	
