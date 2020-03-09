from flask import Flask, request

app = Flask(__name__)

connect=False

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
    app.run()
