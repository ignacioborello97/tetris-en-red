TODO LIST
=========

Cliente:
--------
- aprender a testear pygame
    - probar testear con unittest
    - si no funciona unit test encontrar alguna libreria que agunte pygame

- diseñar las 6 pantallas del juego
    - Diseñar pantalla de login
    - Diseñar pantalla de inicio
    - Diseñar pantalla de unirse a partida
    - Diseñar pantalla de lobby
    - Diseñar pantalla de Tablero de juego
    - Diseñar pantalla de Configuracion

- modelar las piezas de juego [S,Z,L,J,T,I] --> poder dibujarlas en pantalla en base a una clase
    - Modelar S (como se dibuja en la pantalla)
    - Modelar Z (como se dibuja en la pantalla)
    - Modelar L (como se dibuja en la pantalla)
    - Modelar J (como se dibuja en la pantalla)
    - Modelar T (como se dibuja en la pantalla)
    - Modelar I (como se dibuja en la pantalla)
    - En el mejor de los casos, que tome el template de puntitos y caracteres y que dibuje solo en base a eso

- modelar tablero --> poder dibujarlo en pantalla en base a una clase
    
- programar capturas de teclado para el teclado --> capturar cuando se apreta el teclado y diferenciar que tecla es (una forma puede ser la que se usa en server/views/prueba.py)
    - programar funcion que capture cuando se presione una tecla
    - definir teclas para las distintas acciones del juego
    - definir funciones con los comportamientos de las teclas en para los menus
    - definir funciones con los comportamientos de las teclas en para el juego

- experimentar con peticiones http --> con esto hariamos las interacciones de los menus, traer y llevar datos, etc
    - aprender a usar la libreria de peticiones http de python\
    - lograr hacer una peticion get con una query y que acepte un JSON
    - lograr hacer una peticion post con un body en JSON

- experimentar con socket.io(cliente) --> con esto hariamos las interacciones durante el juego
    - aprender a iniciar un cliente
    - definir funciones que se ejecuten al recibir cierto evento
    - definir funcion que se ejecute al conectarse
    - definir funcion que se ejecute al desconectarse
    - enviar eventos con datos

- ver como vamos a hacer reproducir la musiquita de fondo
    - encontrar libreria de sonido de python
    - reproducir un sonido al tocar una tecla
    - reproducir una cancion de fondo
    - lograr que la cancion de fondo se repita cuando termine

Server:
-------
- definir rutas para las peticiones de datos
- implementar interacciones entre usuarios, juegos y tableros
- definir funcionalidad de niveles de juego
- diferenciar una linea de un tetris (4 lineas juntas)
- investigar implementacion de AWS
- implementar socket.io(servidor)