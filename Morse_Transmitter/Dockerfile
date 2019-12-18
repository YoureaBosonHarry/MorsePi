FROM python:3.7.4-buster
WORKDIR /Morse_Transmitter
COPY . /Morse_Transmitter
RUN pip3 install flask numpy requests
ENTRYPOINT ["python3", "Text_To_Morse.py"]
