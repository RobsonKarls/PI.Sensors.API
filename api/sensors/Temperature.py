from random import randint
import os
import datetime

class Temperature:

    def __init__(self):
        self.ds18b20 = ''

    def read(self):
    #	global ds18b20
        self.setup()
        location = '/sys/bus/w1/devices/' + self.ds18b20.lower() + '/w1_slave'
        tfile = open(location)
        text = tfile.read()
        tfile.close()
        secondline = text.split("\n")[1]
        temperaturedata = secondline.split(" ")[9]
        temperature = float(temperaturedata[2:])
        temperature = temperature / 1000
        return temperature

    def setup(self):
        for i in os.listdir('/sys/bus/w1/devices'):
            if i != 'w1_bus_master1':
                self.ds18b20 = str(i)