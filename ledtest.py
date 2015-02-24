#!/user/bin/python
import time
import RPi.GPIO as GPIO
led = 15
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)

repeat = 10
while (repeat > 0):
	print 'Count is ', repeat
	GPIO.output(led, False)
	time.sleep(1)
	GPIO.output(led, True)
	time.sleep(1)
	repeat = repeat - 1

GPIO.cleanup()
