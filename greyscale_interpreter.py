from greyscale_class import GreyscaleSensor
from picarx_improved import Picarx
import time
import logging

logging_format = "%(asctime)s : %(message)s "
logging.basicConfig( format = logging_format, level = logging.DEBUG, datefmt ="%H:%M:%S")
logging.getLogger().setLevel( logging.DEBUG )

class GreyscaleInterpreter():
    def __init__(self):
        self.sensor = GreyscaleSensor()

        #Default value for the light/dark cutoff
        self.default_cutoff = 800

        #Default change in value to detect an edge
        self.default_edge_shift = 200

        self.vals = []
        self.edges = [0, 0]

        #Slope polarization: -1 is outside to in, 0 is no edge, 1 is inside to out
        self.slopes = [0, 0]
        self.interpreted_vals = ["", "", ""]

    def get_sensor_vals(self):
        self.vals = self.sensor.query_sensor()
        for num, val in enumerate(self.vals):
            if val >= self.default_cutoff:
                self.interpreted_vals[num] = "LIGHT"
            else:
                self.interpreted_vals[num] = "DARK"
        logging.debug(f"Interpreted vals: {self.interpreted_vals}")

    def detect_edges(self):
        vals = self.vals
        if abs(vals[0] - vals[1]) >= self.default_edge_shift:
            self.edges[0] = abs(vals[0] - vals[1])
            self.slopes[0] = int(vals[0] < vals[1]) - int(vals[0] > vals[1])
        else:
            self.edges[0] = 0
            self.slopes[1] = 0
        if abs(vals[1] - vals[2]) >= self.default_edge_shift:
            self.edges[1] = abs(vals[1] - vals[2])
            self.slopes[1] = int(vals[2] < vals[1]) - int(vals[2] > vals[1])
        else:
            self.edges[1] = 0
            self.slopes[1] = 0
        logging.debug(f"Edge detected?: {self.edges}")

    def centering(self):
        logging.debug(f"Centering: {(self.edges[0]-self.edges[1])/self.default_edge_shift/2}")
        if self.slopes[0] == self.slopes[1]:
            return 0
        elif self.slopes[0] < self.slopes[1]:
            return -1*abs(self.edges[0]+self.edges[1])/(2*max(self.vals))
        elif self.slopes[1] < self.slopes[0]:
            return abs(self.edges[0]+self.edges[1])/(2*max(self.vals))

if __name__=="__main__":
    car = Picarx()
    time.sleep(0.5)
    interpeter = GreyscaleInterpreter()
    while True:
        interpeter.get_sensor_vals()
        interpeter.detect_edges()
        interpeter.centering()
        time.sleep(0.2)