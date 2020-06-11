from .Observer import Observer

class GameSubject(Observer):
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)
    
    def unsubscribe(self, observer):
        self.observers.remove(observer)
    
    def unsubscribe(self, observer):
        self.observers.remove(observer)
