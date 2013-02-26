import logging

"""
The observable class provides basic functionality to notify registered 
observers on changes.
"""
class Observable():
    def __init__(self):
        self._observers = []

    def register(self, observer):
        self._assertObserverCallback(observer)
        if not observer in self._observers:
            self._observers.append(observer)

    def unregister(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

    def _assertObserverCallback(self, observer):
        # must have update method
        assert hasattr(observer,'update')
        # update must accept at least one argument
        #not working: assert observer.update.func_code.co_argcount > 0

