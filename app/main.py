from flask import Flask, request
import cv2
import sys
import numpy

app = Flask(__name__)

connect=False
im

@app.route('/')
def index():
    return "Hi this is the ROV winner's server :) just have fun"

def get_frame():
    camera_port=0
    camera=cv2.VideoCapture(camera_port) #this makes a web cam object

    while True:
        retval, im = camera.read()
        imgencode=cv2.imencode('.jpg',im)[1]
        stringData=imgencode.tostring()
        yield (b'--frame\r\n'
            b'Content-Type: text/plain\r\n\r\n'+stringData+b'\r\n')

    del(camera)

@app.route('/camera1')
def camera1():
     return Response(get_frame(),mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/joy')
def joy():
    if not connect: return "must connect first"
    #send arduino
    joystick = request.args.get('joystick')
    ssendToArduinoend(joystick) 
    return joystick

@app.route('/connect')
def connect():
    connect = not connect
    return str(connect)


def sendToArduino(x):
    #codefsdfkgjdfshfllkdngkbkfkjbhfdkhdfjk
    pass
    
if __name__ == '__main__':
    app.run(threaded=True)
