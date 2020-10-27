import os
import time

print("hi")

while True:
    os.system("iobroker state set tuya.0.85873706cc50e3c9e7a4.5 ff00000000ffff")
    os.system("iobroker state set tuya.0.85873706cc50e3c9e7a4.5 00ff000000ffff")
    os.system("iobroker state set tuya.0.85873706cc50e3c9e7a4.5 0000ff0000ffff")