import PCF8591 as ADC
import RPi.GPIO as GPIO
import time
import math

class Flame:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.DO = 17
        self.setup()

    def setup(self):
        ADC.setup(0x48)
        GPIO.setup(self.DO, GPIO.IN)

    def read(self):
        print ADC.read(0)
        tmp = GPIO.input(self.DO)
        return tmp