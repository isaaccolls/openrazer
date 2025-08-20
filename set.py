import sys
from openrazer.client import DeviceManager
from openrazer.client import constants as razer_constants

import colorsys
import random


def random_color():
    rgb = colorsys.hsv_to_rgb(random.uniform(0, 1), random.uniform(0.5, 1), 1)
    return tuple(map(lambda x: int(256 * x), rgb))


def run():
    argument = sys.argv[1] if len(sys.argv) > 1 else 'L'
    if argument == 'h':
        brightness = 85
    elif argument == 'm':
        brightness = 50
    elif argument == 'l':
        brightness = 10
    else:
        brightness = 50
    print("👀 brightness {}".format(brightness))
    # create a devicemanager. this is used to get specific devices
    device_manager = DeviceManager()
    device_manager.sync_effects = False
    print("Found {} Razer devices".format(len(device_manager.devices)))
    for idx, device in enumerate(device_manager.devices):
        print("👉 {} - {} ({})".format(device.name,
              device.type, bool(device.fx.advanced)))
        effects = [attr for attr in dir(
            device.fx) if not attr.startswith('__')]
        print(effects)
        if device.name == 'Razer Blade 15 (2018)':
            device.fx.misc.logo.active = True
            # # by color
            rows, cols = device.fx.advanced.rows, device.fx.advanced.cols
            for row in range(rows):
                for col in range(cols):
                    if row == 0:
                        device.fx.advanced.matrix[row, col] = (0, 0, 255)
                        if col == 1:
                            device.fx.advanced.matrix[row, col] = (255, 0, 0)
                        elif col == 15:
                            device.fx.advanced.matrix[row, col] = (255, 0, 0)
                    elif row == 1:
                        device.fx.advanced.matrix[row, col] = (0, 255, 0)
                        if col == 1 or col == 12 or col == 13 or col == 14:
                            device.fx.advanced.matrix[row, col] = (0, 0, 255)
                        elif col == 15:
                            device.fx.advanced.matrix[row, col] = (255, 0, 0)
                    elif row == 2:
                        device.fx.advanced.matrix[row, col] = (0, 255, 0)
                        if col == 1 or col == 12 or col == 13 or col == 14 or col == 15 or col == 16 or col == 17:
                            device.fx.advanced.matrix[row, col] = (0, 0, 255)
                        elif col == 3:
                            device.fx.advanced.matrix[row, col] = (255, 0, 255)
                    elif row == 3:
                        device.fx.advanced.matrix[row, col] = (0, 255, 0)
                        if col == 1 or col == 11 or col == 12 or col == 15:
                            device.fx.advanced.matrix[row, col] = (0, 0, 255)
                        elif col == 2 or col == 3 or col == 4:
                            device.fx.advanced.matrix[row, col] = (255, 0, 255)
                    elif row == 4:
                        device.fx.advanced.matrix[row, col] = (0, 255, 0)
                        if col == 1 or col == 10 or col == 11 or col == 12 or col == 15:
                            device.fx.advanced.matrix[row, col] = (0, 0, 255)
                        elif col == 13:
                            device.fx.advanced.matrix[row, col] = (255, 0, 255)
                    elif row == 5:
                        device.fx.advanced.matrix[row, col] = (0, 255, 0)
                        if col <= 11 or col == 15:
                            device.fx.advanced.matrix[row, col] = (0, 0, 255)
                        else:
                            device.fx.advanced.matrix[row, col] = (255, 0, 255)
                    # else:
                    #     device.fx.advanced.matrix[row, col] = (255, 255, 255)
            device.fx.advanced.draw()
            # # by color
            # device.fx.static(162, 25, 255)
            device.brightness = brightness
            print("{} done 🔥".format(device.name))
        elif device.name == 'Razer BlackWidow Chroma Tournament Edition':
            # rows, cols = device.fx.advanced.rows, device.fx.advanced.cols
            # for row in range(rows):
            #     for col in range(cols):
            #         if row == 0:
            #             device.fx.advanced.matrix[row, col] = (0,0,255)
            #             if col == 1:
            #                 device.fx.advanced.matrix[row, col] = (255,0,0)
            #             if col == 20:
            #                 device.fx.advanced.matrix[row, col] =(0,255,0)
            #         elif row == 1:
            #             device.fx.advanced.matrix[row, col] =(0,255,0)
            #             if col == 1 or col == 12 or col == 13 or col == 15 or col == 16 or col == 17:
            #                 device.fx.advanced.matrix[row, col] =(0,0,255)
            #             elif col == 14:
            #                 device.fx.advanced.matrix[row, col] =(255,0,0)
            #         elif row == 2:
            #             device.fx.advanced.matrix[row, col] =(0,255,0)
            #             if col == 1 or col == 12 or col == 13 or col == 14 or col == 16 or col == 17:
            #                 device.fx.advanced.matrix[row, col] =(0,0,255)
            #             elif col == 3:
            #                 device.fx.advanced.matrix[row, col] =(255,0,255)
            #             elif col == 15:
            #                 device.fx.advanced.matrix[row, col] =(255,0,0)
            #         elif row == 3:
            #             device.fx.advanced.matrix[row, col] =(0,255,0)
            #             if col == 1 or col == 11 or col == 12 or col == 14:
            #                 device.fx.advanced.matrix[row, col] = (0,0,255)
            #             elif col== 2 or col == 3 or col == 4:
            #                 device.fx.advanced.matrix[row, col] =(255,0,255)
            #         elif row == 4:
            #             device.fx.advanced.matrix[row, col] =(0,255,0)
            #             if col == 1 or col == 10 or col == 11 or col == 12 or col == 14:
            #                 device.fx.advanced.matrix[row, col] = (0,0,255)
            #         elif row == 5:
            #             device.fx.advanced.matrix[row, col] =(0,255,0)
            #             if col <= 14:
            #                 device.fx.advanced.matrix[row, col] = (0,0,255)
            #         else:
            #             device.fx.advanced.matrix[row, col] = (255,255,255)
            # device.fx.advanced.draw()
            # by color
            device.fx.static(0, 255, 0)
            device.brightness = brightness
            print("{} done 🔥".format(device.name))
        elif device.name == 'Razer Basilisk X HyperSpeed':
            print(idx)
            print(device.dpi)
            print(device_manager.devices[idx].dpi)
            print(device_manager.devices[idx]._available_features)
            print("{} done 🔥".format(device.name))
        elif device.name == 'Razer Kraken Ultimate':
            device.fx.breath_single(0, 255, 0)


if __name__ == '__main__':
    run()
