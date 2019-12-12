import os
import numpy as np
import requests
import time

#Define time units in seconds (0.1 = 100 milliseconds)
time_unit = 0.1

# Define Morse Nomenclature Based On Time Unit
off = 0
on = 1
dot = (np.round(time_unit, 1), on)
intra_letter = (np.round(time_unit, 1), off)
dash = (np.round(3 * time_unit, 1), on)
next_letter = (np.round(3 * time_unit, 1), off)
word_space = (np.round(7 * time_unit, 1), off)

morse = {
  'a': [dot, intra_letter, dash, next_letter],
  'b': [dash, intra_letter, dot, intra_letter, dot, intra_letter, dot, next_letter],
  'c': [dash, intra_letter, dot, intra_letter, dash, intra_letter, dot, next_letter],
  'd': [dash, intra_letter, dot, intra_letter, dot, next_letter],
  'e': [dot, next_letter],
  'f': [dot, intra_letter, dot, intra_letter, dash, intra_letter, dot, next_letter],
  'g': [dash, intra_letter, dash, intra_letter, dot, next_letter],
  'h': [dot, intra_letter, dot, intra_letter, dot, intra_letter, dot, next_letter],
  'i': [dot, intra_letter, dot, next_letter],
  'j': [dot, intra_letter, dash, intra_letter, dash, intra_letter, dash, next_letter],
  'k': [dash, intra_letter, dot, intra_letter, dash],
  'l': [dot, intra_letter, dash, intra_letter, dot, intra_letter, dot, next_letter],
  'm': [dash, intra_letter, dash, next_letter],
  'n': [dash, intra_letter, dot, next_letter],
  'o': [dash, intra_letter, dash, intra_letter, dash, next_letter],
  'p': [dot, intra_letter, dash, intra_letter, dash, intra_letter, dot],
  'q': [dash, intra_letter, dash, intra_letter, dot, intra_letter, dot, next_letter],
  'r': [dot, intra_letter, dash, intra_letter, dot, next_letter],
  's': [dot, intra_letter, dot, intra_letter, dot, next_letter],
  't': [dash, next_letter],
  'u': [dot, intra_letter, dot, intra_letter, dash, next_letter],
  'v': [dot, intra_letter, dot, intra_letter, dot, intra_letter, dash, next_letter],
  'w': [dot, intra_letter, dash, intra_letter, dash, next_letter],
  'x': [dash, intra_letter, dot, intra_letter, dot, intra_letter, dash, next_letter],
  'y': [dash, intra_letter, dot, intra_letter, dash, intra_letter, dash, next_letter],
  'z': [dash, intra_letter, dash, intra_letter, dot, intra_letter, dot, next_letter]
}

def char_to_morse(char):
    if char != ' ':
        return morse[char]
    else:
        return [word_space]

def text_to_char(text):
    for i in text:
        morse = char_to_morse(i)
        for j in morse:
            if j[1] == 0:
                url = "http://172.19.0.2/change_pattern?pattern=solid&hex_color=000000&frequency=1"
                r = requests.post(url)
                time.sleep(j[0])
            else:
                url = "http://172.19.0.2/change_pattern?pattern=solid&hex_color=FF0000&frequency=1"
                r = requests.post(url)
                time.sleep(j[0])
                print(r.status_code)
text_to_char("sos")
