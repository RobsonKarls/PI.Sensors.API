
import json
import requests
import datetime
import time
import threading
import math
from api.sensors.Flame import Flame
from api.sensors.GpsReceiver import GpsReceiver
from api.sensors.Temperature import Temperature
from api.sensors.Humiture import read_humiture
from api.sensors.Sound import readSound
from collections import namedtuple

def datetime_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    raise TypeError("Unknown type")

class BackgroundWork(threading.Thread):
    

    def getTemperature(self):
        temperature = Temperature()
        return temperature.read()

    def getFlame(self):
        flame = Flame()
        return flame.read()

    def getSound(self):
        return readSound()

    def getHumiture(self):
        return read_humiture()
    
    def start(self):
        gpsData = GpsReceiver()
        result = namedtuple('result', 'latitude longitude altitude speeding time_utc')
        
        try:
            gpsData.start()
            while True:
                utc_time = gpsData.utc, " + ", gpsData.fix.time
                g = result(gpsData.fix.latitude, gpsData.fix.longitude, gpsData.fix.altitude, gpsData.fix.speed, utc_time)
                snapshot =  {
                    'DeviceId': 99,
                    'BigSound': self.getSound(),
                    #'Time_utc': g.time_utc,
                    'Flame': self.getFlame(),
                    'Temperature': self.getTemperature(),
                    'Speeding': g.speeding,
                    'Latitude': g.latitude,
                    'Altitude': g.altitude,
                    'Humidity': self.getHumiture(),
                    'Longitude': g.longitude
                    #'Datetime': datetime.datetime.now()
                    }

                url = 'http://hackathon2018-env.umbtvgkrye.us-east-2.elasticbeanstalk.com/Api/Snapshot'

                r = requests.post(url, json = snapshot)
                
                print(r.status_code, r.reason, r.text)

                time.sleep(5)
        except:
            #print('Unexpected error:', sys.exc_info()[0])
            print('Unexpected error:')
            raise
        finally:
            gpsData.stop()
            gpsData.join()


        