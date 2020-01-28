import time
from serial.tools import list_ports
from pydobot import Dobot

port = list_ports.comports()[0].device
device = Dobot(port=port, verbose=True)

(x, y, z, r, j1, j2, j3, j4) = device.pose()
print(f'x:{x} y:{y} z:{z} r:{r}')

device.move_to(91, -88, 1, -47, wait=True)
device.move_to(177, -163, -41, -120, wait=True)
device.suck(True)
time.sleep(1)
device.move_to(-75, -238, 34, -110, wait=True)
device.suck(False)
time.sleep(0.5)
device.move_to(91, -88, 1, -47, wait=True)

device.close()
