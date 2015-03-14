#!/user/bin/python
import time
import random
import RPi.GPIO as GPIO

led = 15  
button = 10

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button,GPIO.IN, pull_up_down=GPIO.PUD_UP)


def	TimeReaction():
	start = time.time()
	pressed = False

	while (pressed == False):
		if GPIO.input(button) == 0:
			pressed = True
	
	stop = time.time()
	
	return stop - start

def FlashWait(maxWait):
	waitSec = random.uniform(3, maxWait)
	print "Waiting for {0}".format(waitSec)

	start = time.time()
	while(time.time() - start < waitSec):
		GPIO.output(led, 0)
		time.sleep(0.500)
		GPIO.output(led, 1)
		time.sleep(0.500)
	
	GPIO.output(led, 0)

def DelayedOn(maxWait):
	waitSec = random.uniform(3, maxWait)
	time.sleep(waitSec)
	GPIO.output(led, 0)

def SignalStart():
	i = 3
	while(i > 0):
		GPIO.output(led, 0)
		time.sleep(0.200)
		GPIO.output(led, 1)
		i = i - 1

print "Get ready..."

#FlashWait(10)
SignalStart()
DelayedOn(10)
elapsed = TimeReaction()

print "Reaction time: {0} ".format(elapsed)
GPIO.cleanup()
