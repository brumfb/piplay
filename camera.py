#!/usr/bin/python

import cv2.cv as cv
import time

cv.NamedWindow("camera", 1)

capture = cv.CaptureFromCAM(1)
cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH, 320)
cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT,240)

img = cv.QueryFrame(capture)
cv.ShowImage("camera", img)

while True:
    key = cv.WaitKey(10)
    if key == 27:
        break
    elif key == 112:
	img = cv.QueryFrame(capture)
	cv.ShowImage("camera", img)

cv.DestroyAllWindows()
