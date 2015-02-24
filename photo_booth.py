import RPi.GPIO as GPIO
import cv2
import cv2.cv as cv
import time
import ultrasonic as US

GPIO.setmode(GPIO.BOARD)

US.setup(16,11)

max_range = 9999
cooldown_time = 2

cv.NamedWindow("photobooth", 1)

capture = cv2.VideoCapture()
capture.set(cv.CV_CAP_PROP_FRAME_WIDTH, 320)
capture.set(cv.CV_CAP_PROP_FRAME_HEIGHT, 240)

#cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH, 320)
#cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT, 240)

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
	#img = cv.QueryFrame(capture)
	# QueryFrame forces you to keep up with frames
	capture.open(-1)
	ok,img=capture.read()	
	if (ok == True):
		cv2.imshow("photobooth", img)
	capture.release()


def is_in_range():
	current_range = US.get_distance()
	return (current_range < max_range)
		
max_range = set_range()

while True:
	if (is_in_range()):
		update_picture()
		time.sleep(cooldown_time)

	key = cv.WaitKey(10)

	if (key == 27):
		break
	elif (key == 114):
		set_range()

cv.DestroyAllWindows()
GPIO.cleanup()

