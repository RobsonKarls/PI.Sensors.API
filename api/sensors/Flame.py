import RPi.GPIO as GPIO
import time
import math
import modules.PCF8591 as ADC

class Flame():
    def __init__(self):
        self.DO = 17

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        ADC.setup(0x48)
        GPIO.setup(self.DO, GPIO.IN)

    def read(self):
        self.setup()
        result = GPIO.input(self.DO)
        return result
