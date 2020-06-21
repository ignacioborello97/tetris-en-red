from ..lib.Subject import Subject


class Controller(Subject):
    instances = []
    observers = []

    def __init__(self, model):
        self.model = model

    def get(self, id):
        for instance in type(self).instances:
            if instance.id == id:
                return instance

    def list(self):
        return type(self).instances

    def set(self, instance_id, data):
        working_instance = None
        for instance in type(self).instances:
            if instance.id == instance_id:
                working_instance = instance
        if working_instance is not None:
            for key in data.keys():
                if hasattr(working_instance, key):
                    setattr(working_instance, key, data[key])
        else:
            working_instance = self.model.from_dict(data)
            type(self).instances.append(working_instance)
            working_instance.subscribe(self)
        return working_instance

    def remove(self, instance_id):
        for instance in type(self).instances:
            if instance.id == instance_id:
                working_instance = instance
        if working_instance is not None:
            type(self).instances.remove(working_instance)
            return True
        else:
            return False

    def emit(self, channel, data):
        for observer in type(self).observers:
            observer.update(channel, data)
