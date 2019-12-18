from flask import Flask, Response, jsonify, request
import curses
import logging
import os
import sys

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

@app.route('/', methods=['POST'])
def print_word():
    json_data = request.get_json()
    print(json_data['word'], file=sys.stdout)
    return Response("OK", 200)

if __name__ == '__main__':
    app.run()