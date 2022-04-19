import sys
from openrazer.client import DeviceManager
from openrazer.client import constants as razer_constants


def run():
    brightness = float(sys.argv[1]) if len(sys.argv) > 1 else 10
    print("👀 brightness {}".format(brightness))
    # create a devicemanager. this is used to get specific devices
    device_manager = DeviceManager()
    device_manager.sync_effects = False
    print("Found {} Razer devices".format(len(device_manager.devices)))
    for idx, device in enumerate(device_manager.devices):
        print("👉 {} - {}".format(device.name, device.type))
        if device.name == 'Razer Blade 15 (2018)':
            device.fx.misc.logo.active
            device.fx.misc.logo.active = True
            device.fx.misc.logo.active = 1
            device.fx.spectrum()
            device.brightness = brightness
            print("{} done 🔥".format(device.name))
        elif device.name == 'Razer BlackWidow Chroma Tournament Edition':
            device.fx.spectrum()
            device.brightness = brightness
            print("{} done 🔥".format(device.name))
        elif device.name == 'Razer Basilisk X HyperSpeed':
            print(idx)
            print(device.dpi)
            print(device_manager.devices[idx].dpi)
            print(device_manager.devices[idx]._available_features)
            print("{} done 🔥".format(device.name))


if __name__ == '__main__':
    run()
