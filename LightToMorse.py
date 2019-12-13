import cv2
import numpy as np
from queue import Queue
import time
from threading import Thread

def detect_light(image):
    pixel_sum = cv2.sumElems(image)
    pixel_sum = np.sum(pixel_sum)
    print(pixel_sum)

cap = cv2.VideoCapture(0)
time.sleep(2)

while True:
    ret, frame = cap.read()
    if type(frame) == type(None):
        break
    detect_light(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
