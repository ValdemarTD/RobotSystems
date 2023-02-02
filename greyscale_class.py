try:
    from ezblock import ADC
except:
    from robot_hat import ADC

import time
import logging
from picarx_improved import Picarx

logging_format = "%(asctime)s : %(message)s "
logging.basicConfig( format = logging_format, level = logging.DEBUG, datefmt ="%H:%M:%S")
logging.getLogger().setLevel( logging.DEBUG )

class GreyscaleSensor():
    def __init__(self):
        self.adc0 = ADC("A0")
        self.adc1 = ADC("A1")
        self.adc2 = ADC("A2")
        self.val_list = [0, 0, 0]
    
    def query_sensor(self):
        self.val_list = [self.adc0.read(), self.adc1.read(), self.adc2.read()]
        logging.debug(f"Greyscale Sensor returned {self.val_list}")
        return self.val_list


if __name__=="__main__":
    car = Picarx()
    sensor = GreyscaleSensor()
    while True:
        sensor.query_sensor()
        time.sleep(0.1)
