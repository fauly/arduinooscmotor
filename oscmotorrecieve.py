#import serial
#import argparse
#from pythonosc import dispatcher
#from pythonosc import osc_server
#osclistenip = '127.0.0.1'
#osclistenport = 40030
#if __name__ == "__main__":
#    parser = argparse.ArgumentParser()
#    parser.add_argument("--ip",default="127.0.0.1", help="The ip to listen on")
#    parser.add_argument("--port",type=int, default=5005, help="The port to listen on")
#    args = parser.parse_args()
#    lmcp = dispatcher.Dispatcher()   
#    dispatcher.map("/Motor1/1",StartMotor())
#    dispatcher.map("/Motor1/-1",ReverseMotor())
#    dispatcher.map("/Motor1/0",StopMotor())    
#    server = osc_server.ThreadingOSCUDPServer((osclistenip,osclistenport),lmcp)
#    print("Serving on {}".format(server.server_address))
#    server.serve_forever()

import types
import serial

from OSC import OSCServer
from time import sleep

anerrormessage = "beep boop, failed to compute, no device found on: '" 
anworkmessage = "ayyyyy cap'n, gold be a plunder on '"
devicefound = False

server = OSCServer(('localhost', 8000))

try: 
    ser = serial.Serial('/dev/ttyACM0', 9600) 
    print anworkmessage + "/dev/ttyACM0' arrrrr!"
    devicefound =  True
except:
    print anerrormessage + "/dev/ttyACM0' :("
if devicefound == False:
    try:
        ser = serial.Serial('/dev/ttyACM1', 9600)
        print anworkmessage + "/dev/ttyACM1' arrrrr!"
        devicefound = True
    except:
        print anerrormessage + "/dev/ttyACM1' :("
if devicefound == False:
    try:
        ser = serial.Serial('/dev/ttyACM2',9600)
        print anworkmessage + "/dev/ttyACM2' arrrrr!"
        devicefound = True
    except:
        print anerrormessage + "/dev/ttyACM2' :("
if devicefound == False:
    try: 
        ser = serial.Serial('/dev/ttyACM3',9600)
        print anworkmessage + "/dev/ttyACM3' arrrrr!"
        devicefound = True
    except:
        print anerrormessage + "/dev/ttyACM3' :("
if devicefound == False:
    try:
        ser = serial.Serial('/dev/ttyACM4',9600)
        print anworkmessage + "/dev/ttyACM4' arrrrr!"
    except:
        print anerrormessage + "/dev/ttyACM4' :("
def handle_timeout(self):
    self.timed_out = True

def motorGo(state):
    if state == 1:
        print "Going forward!"
        ser.write('1')
    elif state == 2:
        print "Backin up!"
        ser.write('2')
    else:
        print "oh christ..."

def motorStop():
    print "Hold it there motor man!"
    ser.write('0')

def motor_callback(path, tags, args, source):
    state = args[0]
    print state
    if path=="/lmcp/motor":
        if state=='1':
            motorGo(1)
        elif state=='2':
            motorGo(2)
        else:
            motorStop()

def handle_error(self,request,client_address):
    pass

server.addMsgHandler( "/lmcp/motor",motor_callback)

server.handle_error = types.MethodType(handle_error, server)

server.timed_out = False

while not server.timed_out:
    server.handle_request()

server.close()
