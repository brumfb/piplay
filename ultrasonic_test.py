import RPi.GPIO as GPIO
import time
import ultrasonic as US

GPIO.setmode(GPIO.BOARD)

US.setup(16, 11)

distance = US.get_distance()

print "Distance (cm): %.1f" % distance

GPIO.cleanup()
