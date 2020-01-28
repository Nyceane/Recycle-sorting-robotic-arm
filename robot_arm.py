######## Moving Dobot Arm #########
#
# Author: Peter Ma
# Date: 1/20/20
# Description: 
# This program moves dobot arm



# Import packages
import threading
import time
from serial.tools import list_ports
from pydobot import Dobot

port = list_ports.comports()[0].device
device = Dobot(port=port, verbose=True)
isRoboticActive=False

thread_left = threading.Thread(target=_robotic_left, daemon=True)
thread_right = threading.Thread(target=_robotic_right, daemon=True)

def _robotic_left():
    (x, y, z, r, j1, j2, j3, j4) = device.pose()
    print(f'x:{x} y:{y} z:{z} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')
    if isRoboticActive == False:
        isRoboticActive = True
        device.move_to(96, 100, -12, -47, wait=False)
        device.move_to(166, -211, -52, -47, wait=False)
        device.suck(True)
        time.sleep(1)
        device.move_to(300, 7, 15, 5, wait=False)
        device.suck(False)
        time.sleep(0.5)
        device.move_to(96, 100, -12, -47, wait=False)
        isRoboticActive = False

def _robotic_right():
    (x, y, z, r, j1, j2, j3, j4) = device.pose()
    print(f'x:{x} y:{y} z:{z} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')
    if isRoboticActive == False:
        isRoboticActive = True
        device.move_to(96, 100, -12, -47, wait=False)
        device.move_to(166, -211, -52, -47, wait=False)
        device.suck(True)
        time.sleep(1)
        device.move_to(-125, -255, 33, -120, wait=False
        device.suck(False)
        time.sleep(0.5)
        device.move_to(96, 100, -12, -47, wait=False)
        isRoboticActive = False

def _robotic_home(direction):
    (x, y, z, r, j1, j2, j3, j4) = device.pose()
    print(f'x:{x} y:{y} z:{z} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')
    if isRoboticActive == False:
        device.move_to(96, 100, -12, -47, wait=False)
        device.suck(False)

def _move_robotic_arm(direction):
    if direction == "left" and isRoboticActive == False:
        thread_left.start()
    elif direction == "right" and isRoboticActive == False:
        thread_right.start()



# Clean up
device.close()

