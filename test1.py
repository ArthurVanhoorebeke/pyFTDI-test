from pyftdi.ftdi import Ftdi
from pyftdi.gpio import GpioController
from time import sleep

#Check if nth bit is set
#E.G: Is 3d bit set in number 5? --> 5 = 101
#Shift number (3-2) times=> 1.
def checkBit(bit,number):
  x = number >> (bit-1) & 1
  if x == 1:
    return True
  else:
    return False


ft232h = GpioController()

ft232h.configure("ftdi://ftdi:ft232h/1")

print("connected? " + str(ft232h.is_connected))
print(ft232h.pins)

ft232h.set_direction(0xFF,0x08)

while True:
  if checkBit(8,ft232h.read() ):
    print("input in D7 is TRUE => light ON")
    ft232h.write(0X08)
  else:
    print("light OFF")

  
ft232h.close()




