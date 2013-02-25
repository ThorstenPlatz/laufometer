import RPIO
import time
import logging
from triggers import InputTrigger
import signal
import sys
import os

logging.basicConfig(level=logging.DEBUG)

pid = str(os.getpid())
pidfile = "./pid"

if os.path.isfile(pidfile):
	logging.error("%s already exists, exiting" % pidfile)
	sys.exit()
else:
	f = open(pidfile, 'wt', encoding='utf-8')
	f.write(pid)
	f.close()


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

logging.debug("Using following configuration:")
logging.debug("- detection pin: %s" % inPin)
logging.debug("- power supply pin: %s" % outPin)


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
		msg = "Selftest failed. Readout should have been (False, True), but was (", r1, ", ", r2, ")."
		logging.error(msg)
		raise Exception(msg)
	else:
		logging.info("Selftest ok.")

def inputCallback(gpio_id, value):
	r = RPIO.input(gpio_id)
	logging.debug("GPIO %s triggered with %s and read %s" % (gpio_id, value, r))


def signal_handler(signal, frame):
	logging.debug("Received SIGINT.")
	shutdownApplication()

def shutdownApplication():
	logging.info("Application is shutting down...")
	trigger.stop()
	trigger.join()
	logging.info("Application shut down complete. Done.")

	# cleanup pidfile
	os.unlink(pidfile)
	sys.exit(0)

######################################


initPins()
selftest()

trigger = InputTrigger(inPin)
trigger.start()

#waitTime = 15
#print("Wating for %s seconds, then stopping trigger..." % waitTime)
#time.sleep(waitTime)

# muss noch angepasst werden
signal.signal(signal.SIGINT, signal_handler)
print("InputTriggers running...")
print("Press Ctrl+C to terminate.")
print("...")
signal.pause()


