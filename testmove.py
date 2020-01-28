import time
from serial.tools import list_ports
from pydobot import Dobot

port = list_ports.comports()[0].device
device = Dobot(port=port, verbose=True)

(x, y, z, r, j1, j2, j3, j4) = device.pose()
print(f'x:{x} y:{y} z:{z} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')

device.move_to(96, 100, -12, -47, wait=False)
device.move_to(166, -211, -52, -47, wait=False)
device.suck(True)
time.sleep(1)
device.move_to(300, 7, 15, 5, wait=False)
device.suck(False)
time.sleep(0.5)
device.move_to(96, 100, -12, -47, wait=False)

device.close()
