from openrazer.client import DeviceManager
from openrazer.client import constants as razer_constants

# Create a DeviceManager. This is used to get specific devices
device_manager = DeviceManager()

print("Found {} Razer devices".format(len(device_manager.devices)))
for device in device_manager.devices:
    print("{} - {}".format(device.name, device.type))
    if device.name == 'Razer Blade 15 (2018)':
        device.fx.misc.logo.active
        device.fx.misc.logo.active = True
        device.fx.misc.logo.active = 1
        # device.fx.spectrum()
        device.fx.static(0, 255, 0)
        device.brightness = 15
    elif device.name == 'Razer BlackWidow Chroma Tournament Edition':
        # device.fx.spectrum()
        device.fx.static(0, 255, 0)
        device.brightness = 50
