#!/user/bin/python
import time
import RPi.GPIO as GPIO
button = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(button,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

lastPressedState = False

while (True):
	pressedState = GPIO.input(button)
	if (lastPressedState != pressedState):
		if pressedState:
			print("Pressed!")
		else:
			print("Released!")

		lastPressedState = pressedState

GPIO.cleanup()
