from abc import ABC, abstractmethod


# Abstract Based Class
class Switchable(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_of(self):
        pass


# Implements the interface defined by Switchable
class LightBulb(Switchable):
    def turn_on(self):
        print("Light bulb turned on")

    def turn_of(self):
        print("Light bulb turned off")


class Fan(Switchable):
    def turn_on(self):
        print("Fan turned on")

    def turn_of(self):
        print("Fan turned off")


# We removed the dependency between the light bulb and the electric switch
# using dependency inversion
class ElectricPowerSwitch:

    def __init__(self, c: Switchable):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_of()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True


if __name__ == "__main__":
    l_1 = LightBulb()
    f_1 = Fan()
    switch = ElectricPowerSwitch(l_1)
    switch.press()
    switch.press()
    switch_2 = ElectricPowerSwitch(f_1)
    switch_2.press()
