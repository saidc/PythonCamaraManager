# camera and video capture
import cv2
import numpy as np 

capture = cv2.VideoCapture(0)
while True:
    ret, frame = capture.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
