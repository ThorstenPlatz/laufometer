from datetime import datetime
from common.observable import Observable

"""
The EventRecorder is a simple class that keeps track of the time, events occur.
"""
class EventRecorder(Observable):
    def __init__(self):
        Observable.__init__(self)
        self._events = []

    def recordEvent(self):
        now = datetime.now()
        self._events.append(now)
        self.notify()

    def events(self):
        return self._events

    def clearEvents(self):
        self._events = []

    def update(self, observable):
        self.recordEvent()


