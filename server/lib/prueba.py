import threading
import random
from .Observer import Observer
from .Subject import Subject

class alguien:
    def __init__(self, name):
        self.name = name

    def saludar(self, quien):
        print('hola '+str(quien)+' me llamo '+self.name)

def funcion_a_ejecutar(value):
    print('oh recibi el valor ' + str(value))

a_subject = Subject()

pablo = alguien('pablo')
juan = alguien('juan')
pepe = alguien('pepe')

observer_1 = Observer(pablo.saludar)
observer_2 = Observer(juan.saludar)
observer_3 = Observer(pepe.saludar)

a_subject.subscribe(observer_1)
a_subject.subscribe(observer_2)
a_subject.subscribe(observer_3)


def next():
    lista = ['a','b','c','d']

    a_subject.next(random.choice(lista))
    print(' ')
    print(' ')
    threading.Timer(1.4, next).start()

threading.Timer(1.4, next).start()

