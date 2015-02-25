import io
import RPi.GPIO as GPIO
import picamera
import picamera.array
import cv2
import time
import ultrasonic as US
import numpy as np


GPIO.setmode(GPIO.BOARD)

US.setup(16,11)

max_range = 9999
cooldown_time = 2


camera = picamera.PiCamera()
camera.resolution=(640,480)
camera.vflip = True

cv2.namedWindow("photobooth", 1)

def set_range(samples = 3):
	total = 0
	count = 0
	while (count < samples):
		range = US.get_distance()
		total = total + range
		count = count + 1

	avg = total /samples
	print "Range set to %.2f" % avg
	return avg


def update_picture():
	print "Taking picture"
	stream = io.BytesIO()
	camera.capture(stream, format='jpeg')
	data = np.fromstring(stream.getvalue(), dtype=np.uint8)
	image = cv2.imdecode(data, 1)
	cv2.imshow("photobooth", image)

def is_in_range():
	current_range = US.get_distance()
	return (current_range < max_range)
		
max_range = set_range()

while True:
	if (is_in_range()):
		update_picture()
		time.sleep(cooldown_time)

	key = cv2.waitKey(30)

	if (key == 27):
		break
	elif (key == 114):
		set_range()

camera.close()
cv2.destroyAllWindows()
GPIO.cleanup()

