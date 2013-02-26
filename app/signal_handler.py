import signal
from common.observable import Observable

"""
The SigIntHandler does exactly what it's name suggests, it handles the 
SIGINT signal. It can be used as an observable which notifies it's 
observers when a SIGINT was caught. Use waitForSignal() to block the 
caller thread until a signal is received. 
NOTICE that python does only allow signal trapping in the main thread
of the application.
"""
class SigIntHandler(Observable):
    def __init__(self):
        Observable.__init__(self)
        signal.signal(signal.SIGINT, self._signalHandler)
        
    def waitForSignal(self): 
        signal.pause()
        
    def _signalHandler(self, signal, frame):
        self.notify()
