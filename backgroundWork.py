
import json
import requests
import datetime
import time
import threading
import math
from api.sensors.Flame import Flame
from api.sensors.GpsReceiver import GpsReceiver
from api.sensors.Humiture import read_humiture
from api.sensors.Sound import Sound
from collections import namedtuple

class BackgroundWork(threading.Thread):

    def getTemperature(self):
        return 1

    def getFlame(self):
        flame = Flame()
        return flame.read()

    def getSound(self):
        sound = Sound()
        return sound.read()

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
                    'Time_utc': g.time_utc,
                    'Flame': self.getFlame(),
                    'Temperature': 24,
                    'Speeding': g.speeding,
                    'Latitude': g.latitude,
                    'Altitude': g.altitude,
                    'Humidity': self.getHumiture(),
                    'Longitude': g.longitude,
                    'Datetime': datetime.datetime.now()
                    }

                url = 'http://hackathon2018-env.umbtvgkrye.us-east-2.elasticbeanstalk.com/Api/Snapshot'

                r = requests.post(url, data = snapshot)
                print(r.status_code, r.reason, r.text)

                time.sleep(5)
        except:
            #print('Unexpected error:', sys.exc_info()[0])
            print('Unexpected error:')
            raise
        finally:
            gpsData.stop()
            gpsData.join()

    if __name__ == '__main__':
        bgWork = BackgroundWork()
        bgWork.start()

        