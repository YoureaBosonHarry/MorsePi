import cv2
import numpy as np
import os
import requests
import time

screen_endpoint = os.environ.get("SCREENENDPOINT", None)

frame_rate = 10
last_frame = 0
led_constant = 1.1
time_constant = np.round(1/frame_rate, 1)
running_average = 0
number_of_frames = 0
running_sum = 0
on = 0
off = 0
state = "off"
morse_list = []
morse = {"on": {time_constant: "dot", 3*time_constant: "dash"}, "off": {time_constant: "intra_letter", 3*time_constant: "next_letter", 7*time_constant: "word_space"}}

morse_to_letter = {
"dot intra_letter dash": "a",
"dash intra_letter dot intra_letter dot intra_letter dot": "b",
"dash intra_letter dot intra_letter dash intra_letter dot": "c",
"dash intra_letter dot intra_letter dot": "d",
"dot": "e",
"dot intra_letter dot intra_letter dash intra_letter dot": "f",
"dash intra_letter dash intra_letter dot": "g",
"dot intra_letter dot intra_letter dot intra_letter dot": "h",
"dot intra_letter dot": "i",
"dot intra_letter dash intra_letter dash intra_letter dash": "j",
"dash intra_letter dot intra_letter": "k",
"dot intra_letter dash intra_letter dot intra_letter dot": "l",
"dash intra_letter dash": "m",
"dash intra_letter dot": "n",
"dash intra_letter dash intra_letter dash": "o",
"dot intra_letter dash intra_letter dash intra_letter": "p",
"dash intra_letter dash intra_letter dot intra_letter dot": "q",
"dot intra_letter dash intra_letter dot": "r",
"dot intra_letter dot intra_letter dot": "s",
"dash": "t",
"dot intra_letter dot intra_letter dash": "u",
"dot intra_letter dot intra_letter dot intra_letter dash": "v",
"dot intra_letter dash intra_letter dash": "w",
"dash intra_letter dot intra_letter dot intra_letter dash": "x",
"dash intra_letter dot intra_letter dash intra_letter dash": "y",
"dash intra_letter dash intra_letter dot intra_letter dot": "z"
} 

def detect_light(image):
    global last_frame
    global on
    global off
    global state
    global running_average
    global number_of_frames
    global running_sum
    global morse_list
    if number_of_frames == 100000:
        number_of_frames = 0
        running_sum = 0
    pixel_sum = cv2.sumElems(image)
    pixel_sum = np.sum(pixel_sum)
    running_sum += pixel_sum
    number_of_frames += 1
    running_average = int(running_sum/number_of_frames)
    if pixel_sum > led_constant*running_average:
        off = 0
        state = "on"
        on += time_constant
    else:
        if state == "on":
            try:
                if on < 3*time_constant:
                    morse_list.append(morse[state][time_constant])
                elif on >= 3*time_constant and on < 7*time_constant:
                    morse_list.append(morse[state][3*time_constant])
                print(morse_list)
            except:
                pass
        off += time_constant
        if off >  9*time_constant:
            morse_list = []
        elif off > 0 and off < 2*time_constant:
            morse_list.append("intra_letter")
        elif off >= 2*time_constant and off <= 4*time_constant:
            morse_list.append("next_letter")
        elif off >= 6*time_constant and off <= 8*time_constant:
            morse_list.append("word_space")
            print_word(morse_list)
            morse_list = []
        on = 0
        state = "off"

def print_word(morse_word):
    letter = ""
    word = []
    for i in morse_word:
        if i == "next_letter":
            word.append(morse_to_letter[letter.strip()])
            letter = ""
        else:
            letter += "".join(f"{i} ")
    joined_word = "".join(i for i in word)
    requests.post(screen_endpoint, json={"word": joined_word})

def capture_morse():
    cap = cv2.VideoCapture(0)
    print("[INFO] Camera Warming Up...")
    time.sleep(2)

    while True:
        ret, frame = cap.read()
        if type(frame) == type(None):
            break
        detect_light(frame)
        time.sleep(1/frame_rate)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == '__main__':
    print("[INFO] Beginning Capture...")
    capture_morse()