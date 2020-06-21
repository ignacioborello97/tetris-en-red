class Observer:

    def __init__(self):
        self.subjects = []

    def update(self, channel: str, value):
        pass

    def subscribe(self, subject):
        self.subjects.append(subject)
        subject.observers.append(self)
