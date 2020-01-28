import time
from serial.tools import list_ports
from pydobot import Dobot

port = list_ports.comports()[0].device
device = Dobot(port=port, verbose=False)

while True:
    (x, y, z, r, j1, j2, j3, j4) = device.pose()
    print(f'x:{x} y:{y} z:{z} r:{r}')

device.close()
