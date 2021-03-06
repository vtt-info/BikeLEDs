import random
import time

from functions.driving_animation import DrivingAnimation
from functions.rainbow_animation import RainbowAnimation
from functions.testleds import TestLEDs
from functions.turn_animation import TurnAnimation


class Bike():
    def __init__(self, test=False):
        if not test:
            from neopixel import NeoPixel
            from machine import Pin

        self.leds_front = NeoPixel(
            Pin(5, Pin.OUT), 30, bpp=3) if not test else TestLEDs(30)
        self.leds_left = NeoPixel(
            Pin(17, Pin.OUT), 5, bpp=3) if not test else TestLEDs(5)
        self.leds_right = NeoPixel(
            Pin(18, Pin.OUT), 5, bpp=3)if not test else TestLEDs(5)
        self.mode = 'relaxed'
        self.time_passed = 0
        self.animation_brightness = 0.0
        self.animation_direction = 'up'
        self.animation_up_and_down = True
        self.test = test

    def start_driving(self):
        while True:
            # check if mode has changed
            self.switches = {
                'left': self.switch_left,
                'right': self.switch_right
            }

            if self.switches['left'] == True and self.switches['right'] == True:
                self.mode = 'relaxed'
                self.rainbow_animation()

            elif self.switches['left'] == False and self.switches['right'] == False:
                self.mode = 'safe'
                self.driving_animation()

            elif self.switches['left'] == True:
                self.mode = 'turn_left'
                self.turn_left()

            elif self.switches['right'] == True:
                self.mode = 'turn_right'
                self.turn_right()

            self.leds_left.write()
            print()
            self.leds_front.write()
            print()
            self.leds_right.write()
            print()
            print()

            time.sleep(1.0/36.0)

    @property
    def switch_left(self):
        if self.test:
            return True
        # placeholder pin
        return Pin(10, Pin.OUT)

    @property
    def switch_right(self):
        if self.test:
            return True
        # placeholder pin
        return Pin(11, Pin.OUT)

    def turn_right(self):
        self = TurnAnimation(bike=self, direction='right').bike

    def turn_left(self):
        self = TurnAnimation(bike=self, direction='left').bike

    def rainbow_animation(self):
        # relaxed mode
        self = RainbowAnimation(bike=self).bike

    def driving_animation(self):
        # safe mode
        self = DrivingAnimation(bike=self).bike


Bike(test=True).start_driving()
