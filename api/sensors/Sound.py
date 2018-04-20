#!/usr/bin/env python
import PCF8591 as ADC
import RPi.GPIO as GPIO

class Sound():

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        ADC.setup(0x48)

    def read(self):
        self.setup()
        result = ADC.read(0)
        if result < 150:
            return 1
        else:
            return 0
                
            


