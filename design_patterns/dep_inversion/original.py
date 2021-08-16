class LightBulb:
    def turn_on(self):
        print("Light bulb turned on")

    def turn_of(self):
        print("Light bulb turned off")


class ElectricPowerSwitch:

    def __init__(self, lb: LightBulb):
        self.light_bulb = lb
        self.on = False

    def press(self):
        if self.on:
            self.light_bulb.turn_of()
            self.on = False
        else:
            self.light_bulb.turn_on()
            self.on = True


if __name__ == "__main__":
    l_1 = LightBulb()
    switch = ElectricPowerSwitch(l_1)
    switch.press()
    switch.press()
