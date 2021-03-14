from bluepy.btle import Peripheral


# Brightness in percent (0-100)
def brightness(percent):
    return [0x7e, 0x00, 0x01, percent, 0x00, 0x00, 0x00, 0x00, 0xef]


# Color in hexadecimal format (ex: #FF00FF)
def color(hexa):
    hexa = hexa[1:]
    return [0x7e, 0x07, 0x05, 0x03, int(hexa[0:2], 16), int(hexa[2:4], 16), int(hexa[4:6], 16), 0x00, 0xef]


class Led:
    currentColor = '#FF00FF'
    currentBrightness = 100

    def __init__(self, address, uuid, characteristic):
        self.uuid = uuid
        self.address = address

        self.peripheral = Peripheral(address)
        self.service = self.peripheral.getServiceByUUID(uuid)
        self.device = self.service.getCharacteristics(characteristic)[0]

        self.set_brightness(self.currentBrightness)
        self.set_color(self.currentColor)

    # Set brightness intensity in percent
    def set_brightness(self, b):
        self.currentBrightness = b
        self.device.write(bytearray(brightness(b)))

    # Set color in hexadecimal format (ex: #FF00FF)
    def set_color(self, c):
        self.currentColor = c
        self.device.write(bytearray(color(c)))

    def stop(self):
        self.peripheral.disconnect()
