from flask import Flask, Response, jsonify, request
import os
import Char_To_Morse
import requests
import sys

app = Flask(__name__)
neopixels_endpoint = os.environ.get("NEOPIXELSENDPOINT", None)
neopixels_color = str(os.environ.get("NEOPIXELSCOLOR", "FF0000"))

neopixels_off = f"{neopixels_endpoint}/change_pattern?pattern=solid&hex_color=000000&frequency=1"
neopixels_on = f"{neopixels_endpoint}/change_pattern?pattern=solid&hex_color={neopixels_color}&frequency=1"

def morse_to_neopixels(data):
    for i in data["text"]:
        morse_units = Char_To_Morse.char_to_morse(i.lower())
        for j in morse_units:
            if j[1] == 0:
                requests.post(neopixels_off)
                time.sleep(j[0])
            else:
                requests.post(neopixels_on)
                time.sleep(j[0])

@app.route('/receive_morse', methods=['POST'])
def receive_morse():
    data = request.get_json()
    morse_to_neopixels(data)
    return Response("OK", 200)

if __name__ == '__main__':
    app.run(debug=True)    
