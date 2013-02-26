from datetime import datetime

"""
The EventRecorder is a simple class that keeps track of the time, events occur.
"""
class EventRecorder():
    def __init__(self):
        self._events = []
        
    def recordEvent(self):
        now = datetime.now()
        self._events.append(now)
        
    def events(self):
        return self._events
    
    def update(self, observable):
        self.recordEvent()
