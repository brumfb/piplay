import io
import picamera
import picamera.array
import time
import cv2
import cv2.cv as cv
import numpy as np

camera = picamera.PiCamera()
camera.resolution=(640,480)

cv.NamedWindow("camera", 1)

def update_image():
	stream = io.BytesIO()
	camera.capture(stream, format='jpeg')
	data = np.fromstring(stream.getvalue(), dtype=np.uint8)	
	image = cv2.imdecode(data, 1)
	imagesrc = cv.fromarray(np.array(image[:, :, ::-1]))	
	cv.ShowImage("camera", imagesrc)

update_image()

while True:
	key = cv.WaitKey(10)

	if (key == 27):
		break
	elif (key == 114):
		update_image()


cv.DestroyAllWindows()
camera.close()

