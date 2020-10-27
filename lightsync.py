import os
from colour import Color
import numpy
import pyscreenshot
import time
from colorthief import ColorThief

mode = "average"

while True:
    start = time.time()
    myimg = pyscreenshot.grab()
    c = None
    if mode == "dominant":
        color_thief = ColorThief(myimg)
        c = color_thief.get_color(quality=1)
        print(c)
        c = Color(rgb=(float(c[0]) / 255, float(c[1]) / 255, float(c[2] / 255)))
        print(c)
    elif mode == "average":
        avg_color_per_row = numpy.average(myimg, axis=0)
        avg_color = numpy.average(avg_color_per_row, axis=0)
        c = Color(rgb=(avg_color[0] / 255, avg_color[1] / 255, avg_color[2] / 255))
    end = time.time()
    print(end - start)
    print(c)

    os.system("iobroker state set tuya.0.85873706cc50e3c9e7a4.5 " + c.hex[1:] + "0000ffff")
    os.system("iobroker state set tuya.0.85873706cc50e3c9ebee.5 " + c.hex[1:] + "0000ffff")
    os.system("iobroker state set tuya.0.85873706cc50e3c9ec3b.5 " + c.hex[1:] + "0000ffff")
    # cmd = " c:\\curl\\curl.exe -u \""+TOKEN+":\" -X PUT -d \"color=" + str(c.hex) + "\" -d \"duration=" +str(DURATION)+ "\" \"https://api.lifx.com/v1beta1/lights/label:"+BULB_NAME+"/color\""


