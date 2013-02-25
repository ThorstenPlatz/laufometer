import RPIO
import time
import logging

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
	r = RPIO.input(inPin)
	logging.debug("GPIO %s triggered with %s and read %s" % (gpio_id, value, r))



######################################

logging.basicConfig(level=logging.DEBUG)

initPins()
selftest()

RPIO.add_interrupt_callback(inPin, inputCallback, edge='falling')
RPIO.wait_for_interrupts()

print("done.")

