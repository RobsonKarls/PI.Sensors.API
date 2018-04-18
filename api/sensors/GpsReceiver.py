from gps import *
import time
import threading
import math

class GpsReceiver(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
        self.running = False
    
    def run(self):
        self.running = True
        while self.running:
            # grab EACH set of gpsd info to clear the buffer
            self.gpsd.next()

    def stop(self):
        self.running = False
  
    @property
    def fix(self):
        return self.gpsd.fix

    @property
    def utc(self):
        return self.gpsd.utc

    @property
    def satellites(self):
        return self.gpsd.satellites

if __name__ == '__main__':
    # create the controller
    gpsReceiver = GpsReceiver() 
    try:
        # start controller
        gpsReceiver.start()
        while True:
            print("latitude ", gpsReceiver.fix.latitude)
            print("longitude ", gpsReceiver.fix.longitude)
            print("time utc ", gpsReceiver.utc, " + ", gpsReceiver.fix.time)
            print("altitude (m)", gpsReceiver.fix.altitude)
            print("eps ", gpsReceiver.fix.eps)
            print("epx ", gpsReceiver.fix.epx)
            print("epv ", gpsReceiver.fix.epv)
            print("ept ", gpsReceiver.gpsd.fix.ept)
            print("speed (m/s) ", gpsReceiver.fix.speed)
            print("climb ", gpsReceiver.fix.climb)
            print("track ", gpsReceiver.fix.track)
            print("mode ", gpsReceiver.fix.mode)
            print("sats ", gpsReceiver.satellites)
            time.sleep(0.5)
    #Ctrl C
    except KeyboardInterrupt:
        print("User cancelled")
        #Error
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

    finally:
        print("Stopping gps controller")
        gpsReceiver.stop()
        #wait for the tread to finish
        gpsReceiver.join()
      
    print("Done")