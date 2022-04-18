#!/usr/bin/python3
from openrazer.client import DeviceManager
import openrazer.client
a = openrazer.client.DeviceManager()
print(a.devices)
# a.turn_off_on_screensaver = False
# for device in a.devices:
#     device.brightness = 100
#     device.fx.static(0, 255, 0)
#     if device.type == "mouse":
#         print("it's a mouse!!")
#         device.poll_rate = 500
