import RPIO
import logging

class Circuit():
    """
    Expects a dictionary with the GPIO ports in the following form:
    configuration
        inPin = <GPIO pin used for scanning for events>
        outPin = <GPIO pin used as power source>  
    
    NOTICE the pin numbering is in RPIO.BCM format.
    """
    def configure(self, configuration):
        self.inPin = configuration['inPin']
        self.outPin = configuration['outPin']
        
        logging.debug("Using following configuration:")
        logging.debug("- detection pin: %s" % self.inPin)
        logging.debug("- power supply pin: %s" % self.outPin)
        
    # Setup pin numbering and input/output pins.
    def init(self):
        RPIO.setmode(RPIO.BCM)
    
        RPIO.setup(self.outPin, RPIO.OUT)
        RPIO.setup(self.inPin, RPIO.IN)
        
        self._selftest()
    
    
    # Perform simple selftest.
    # Checks if the readout works as expected assuming the switch is open.
    def _selftest(self):
        RPIO.output(self.outPin, False)
        r1 = RPIO.input(self.inPin)
    
        RPIO.output(self.outPin, True)
        r2 = RPIO.input(self.inPin)
    
        if r1 != False or r2 != True:
            msg = "Selftest failed. Readout should have been (False, True), but was (", r1, ", ", r2, ")."
            logging.error(msg)
            raise Exception(msg)
        else:
            logging.info("Selftest ok.")