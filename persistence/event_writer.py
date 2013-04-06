import time
from datetime import datetime

"""
The EventRecorder is a simple class that keeps track of the time, events occur.
"""
class EventWriter():
    def __init__(self, filename):
        self._filenamePrefix = filename
        self._filename = None
        self._file = None

    def currentFileName(self):
        today = datetime.now().strftime('%Y-%m-%d')
        filename = self._filenamePrefix + "_" + today
        return filename

    def writeEvents(self, events):
        currentFilename = self.currentFileName()
        if(currentFilename != self._filename):
            if(self._filename is not None):
                self._file.close()
            self._filename = currentFilename
            self._file = open(self._filename, 'at', encoding='utf-8', buffering=1)
        
        for event in events:
            self.appendEvent(self._file, event)
        self._file.flush()

    def appendEvent(self, file, event):
        formattedTime = event.strftime('%Y-%m-%d %H:%M:%S.%f')
        file.write(formattedTime)
        file.write("\n")

    def events(self):
        return self._events

    def update(self, observable):
        self.writeEvents(observable.events())

    def close(self):
        if(self._file is not None):
            self._file.close()

