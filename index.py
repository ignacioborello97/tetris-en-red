import threading
import random

from pynput import keyboard

from server.views.prueba import on_press, tick

listener = keyboard.Listener(
    on_press=on_press)
listener.start()

tick()
# import server.lib.test