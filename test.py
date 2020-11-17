import usb
import usb.util
from pyftdi.ftdi import Ftdi
from pyftdi.gpio import GpioController
from time import sleep

# Test USB
dev = usb.core.find(idVendor=0x0403, idProduct=0x6014)
print(dev)

  
ft232h.close()