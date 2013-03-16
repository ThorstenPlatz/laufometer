import time
from datetime import datetime

"""
The EventRecorder is a simple class that keeps track of the time, events occur.
"""
class EventWriter():
    def __init__(self, filename):
        self._filenamePrefix = filename

    def writeEvents(self, events):
        today = datetime.now().strftime('%Y-%m-%d')
        filename = self._filenamePrefix + "_" + today
        file = open(filename, 'a', encoding='utf-8')
        for event in events:
            self.appendEvent(file, event)
        file.close()

    def appendEvent(self, file, event):
        formattedTime = event.strftime('%Y-%m-%d %H:%M:%S.%f')
        file.write(formattedTime)
        file.write("\n")

    def events(self):
        return self._events

    def update(self, observable):
        self.writeEvents(observable.events())

