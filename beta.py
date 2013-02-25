import RPIO
import time
import logging
from triggers import InputTrigger
import signal
import sys

######################################
# Configuration 
######################################

# Use GPIO.BCM mode for pin numbers

# The output pin used to supply the 3.3V power
outPin = 10

# The input pin used to detect events
inPin = 7


######################################
# End of configuration.
######################################

print ("Using following configuration:")
print ("- detection pin: ", inPin)
print ("- power supply pin: ", outPin)


# Setup pin numbering and input/output pins.
def initPins():
	RPIO.setmode(RPIO.BCM)

	RPIO.setup(outPin, RPIO.OUT)
	RPIO.setup(inPin, RPIO.IN)


# Perform simple selftest.
# Checks if the readout works as expected assuming the switch is open.
def selftest():
	RPIO.output(outPin, False)
	r1 = RPIO.input(inPin)

	RPIO.output(outPin, True)
	r2 = RPIO.input(inPin)

	if r1 != False or r2 != True:
		raise Exception("Selftest failed. Readout should have been (False, True), but was (", r1, ", ", r2, ").")
	else:
		print("Selftest ok.")

def inputCallback(gpio_id, value):
	r = RPIO.input(gpio_id)
	logging.debug("GPIO %s triggered with %s and read %s" % (gpio_id, value, r))


def signal_handler(signal, frame):
        print("You pressed Ctrl+C!")
        shutdownApplication()

def shutdownApplication():
	logging.info("Application is shutting down...")
	trigger.stop()
	trigger.join()
	logging.info("Application shut down complete. Done.")
	sys.exit(0)

######################################

logging.basicConfig(level=logging.DEBUG)

initPins()
selftest()

trigger = InputTrigger(inPin)
trigger.start()

#waitTime = 15
#print("Wating for %s seconds, then stopping trigger..." % waitTime)
#time.sleep(waitTime)

# muss noch angepasst werden
signal.signal(signal.SIGINT, signal_handler)
print("Press Ctrl+C")
signal.pause()


