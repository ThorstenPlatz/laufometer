import logging
import sys
from gpio.triggers import InputTrigger
from app.pid_provider import PidFileProvider
from event.event_recorder import EventRecorder
from gpio.circuit import Circuit
from app.signal_handler import SigIntHandler

######################################
# Configuration 
######################################

# Use GPIO.BCM mode for pin numbers

# The output pin used to supply the 3.3V power
outPin = 10

# The input pin used to detect events
inPin = 7


logging.basicConfig(level=logging.DEBUG)

######################################
# End of configuration.
######################################

class MainApplication():
    def run(self):
        self._pidProvider = PidFileProvider()

        circuitConfig = { 'inPin': inPin, 'outPin': outPin }
        self._circuit = Circuit()
        self._circuit.configure(circuitConfig)
        self._circuit.init()
        
        self._trigger = InputTrigger(self._circuit.inPin)
        self._eventRecorder = EventRecorder()
        
        self._trigger.register(self._eventRecorder)
        self._trigger.start()
        
        self._signalTrap = SigIntHandler()
        self._signalTrap.register(self)
        
    def update(self, observable):
        # if we receive a notification, this means our signal handler got SIGINT
        self.shutdownApplication()

    def shutdownApplication(self):
        logging.info("Application is shutting down...")
        self._trigger.stop()
        self._trigger.join()
        logging.info("Application shut down complete. Done.")
    
        sys.exit(0)