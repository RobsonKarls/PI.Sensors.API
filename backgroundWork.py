
import json
import requests
import datetime
import time
from collections import namedtuple
from api.sensors.GpsReceiver import GpsReceiver

class BackgroundWork():
    
    def getTemperature(self):
        return 1

    def getFlame(self):
        return 'flame'

    def getSound(self):
        return 'sound'

    def getHumiture(self):
        return ''

    def getGpsData(self):
        gpsData = GpsReceiver()
        result = namedtuple('result', 'latitude longitude altitude speeding time_utc')
        
        try:
            gpsData.start()
            r = result(gpsData.fix.latitude, gpsData.fix.longitude, gpsData.fix.altitude, gpsData.fix.speeding, gpsData.fix.time_utc)
            return r
        except:
            #print('Unexpected error:', sys.exc_info()[0])
            print('Unexpected error:')
            
            raise
        finally:
            gpsData.stop()
            gpsData.join()

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
                    'sound': self.getSound(),
                    'time_utc': g.time_utc,
                    'flame': self.getFlame,
                    'temperature': 24,
                    'speeding': g.speeding,
                    'latitude': g.latitude,
                    'altitude': g.altitude,
                    'humiture': self.getHumiture(),
                    'longitude': g.longitude,
                    'datetime': datetime.datetime.now()
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

        