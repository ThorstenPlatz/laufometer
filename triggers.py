import threading
import RPIO
import logging
import time

class InputTrigger(threading.Thread):
	def __init__(self, inPin):
		threading.Thread.__init__(self) 
		self.inPin = inPin

	def run(self):
		logging.debug("InputTrigger running on GPIO %s" % self.inPin)
		RPIO.add_interrupt_callback(self.inPin, self.inputCallback, edge='falling')
		RPIO.wait_for_interrupts()
		logging.debug("InputTrigger on GPIO %s stopped." % self.inPin)

	def stop(self):
		logging.debug("InputTrigger on GPIO %s stopping..." % self.inPin)
		RPIO.stop_waiting_for_interrupts()
		RPIO.del_interrupt_callback(self.inPin)

	def inputCallback(self, gpio_id, value):
        	r = RPIO.input(gpio_id)
	        logging.debug("InputTrigger on GPIO %s triggered with %s and read %s" % (gpio_id, value, r))

