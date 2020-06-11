import socketio
from pynput import keyboard

sio = socketio.Client()
# sio.connect('http://localhost:5000')

@sio.on('return_key_press')
def response(res):
    print('response = ' + res)

def on_press(key):
    key_send = ''
    try:
        if(key.char == 'z'):
            key_send = 'z'
        if(key.char == 'x'):
            key_send = 'x'

    except AttributeError:
        if(key == keyboard.Key.right):
            key_send = 'right'
        if(key == keyboard.Key.left):
            key_send = 'left'
        if(key == keyboard.Key.down):
            key_send = 'down'

    print(key)

    sio.emit('key_press', key_send)



# listener = keyboard.Listener(
#     on_press=on_press)
# listener.start()

class MyCustomNamespace(socketio.ClientNamespace):
    def on_connect(self):
        print('connected to namespace '+self.namespace)
        pass

    def on_disconnect(self):
        print('disconnected from namespace '+self.namespace)
        pass

    def on_ping_response(self, data):
        print('on_ping_response : '+data)


id = input('Enter your game id: ')

print(id)

sio.connect('http://localhost:5000', namespaces=['/game/'+id])
# sio.namespaces.append('/game/'+id)
sio.register_namespace(MyCustomNamespace('/game/'+id))
sio.emit('ping','piiing','/game/'+id)
