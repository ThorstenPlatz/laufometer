import time

"""
The EventRecorder is a simple class that keeps track of the time, events occur.
"""
class EventWriter():
    def __init__(self, filename):
        self._filename = filename

    def writeEvents(self, events):
        file = open(self._filename, 'w', encoding='utf-8')
        for event in events:
            self.appendEvent(file, event)
        file.close()

    def appendEvent(self, file, event):
        formattedTime = time.strftime('%Y-%m-%d %H:%M:%S', event)
        file.write(formattedTime)

    def events(self):
        return self._events

    def update(self, observable):
        self.writeEvents(observable.events())

