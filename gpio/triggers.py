import threading
import logging
import RPIO
from common.observable import Observable

class InputTrigger(threading.Thread, Observable):
        def __init__(self, inPin):
                Observable.__init__(self)
                threading.Thread.__init__(self)
                super(InputTrigger,self).__init__()
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
                self.notify()


