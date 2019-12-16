import cv2
import numpy as np
import time

frame_rate = 10
last_frame = 0
led_constant = 1.1
time_constant = 0.1
running_average = 0
number_of_frames = 0
running_sum = 0
on = 0
state = "off"

morse = {"on": {time_constant: "dot", 3*time_constant: "dash"}, "off": {time_constant: "intra_letter", 3*time_constant: "next_letter", 7*time_constant: "word_space"}}

def detect_light(image):
    global last_frame
    global on
    global state
    global running_average
    global number_of_frames
    global running_sum
    if number_of_frames == 100000:
        number_of_frames = 0
        running_sum = 0
    pixel_sum = cv2.sumElems(image)
    pixel_sum = np.sum(pixel_sum)
    running_sum += pixel_sum
    number_of_frames += 1
    running_average = int(running_sum/number_of_frames)
    if pixel_sum > led_constant*running_average:
        state = "on"
        on += time_constant
        print(on)
    else:
        if state == "on":
            try:
                print(morse[state][on], on)
            except:
                pass
        on = 0
        state = "off"

cap = cv2.VideoCapture(0)
time.sleep(2)

while True:
    ret, frame = cap.read()
    if type(frame) == type(None):
        break
    detect_light(frame)
    time.sleep(1/frame_rate)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
