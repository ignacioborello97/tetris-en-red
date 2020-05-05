import pygame,sys
from pygame.locals import*
from tkinter import *
from tkinter import messagebox
from random import randint

#-----------------------------funciones de menu-----------------------------

def salirJuego():
	
	valor=messagebox.askquestion("Salir","Deseas salir de la aplicacion?")

	if valor=="yes":
		root.destroy()
		pygame.quit()
		sys.exit()

	if valor=="no":
		pass

def infoTetris():

	messagebox.showinfo("Tetris en red","Tetricos\nCopyright © 2020-2020\nVersion 1.0.0 - Build 1214\n\nMusic by Kevin MacLeod\nhttps://incompetech.filmmusic.io/")


def instrucciones():
	
	messagebox.showinfo("Instrucciones","""
		El juego es simple:\n1)Pon tu nombre.\n2)Escoge tu avatar.\n3)Conéctate.\n4)Acomoda con las flechas las piezas que caen para formar líneas.\n5)Diviértete!
				""")

def controles():
	
	messagebox.showinfo("Controles","""Flecha arriba: rota la pieza.\nFlecha abajo: acelera la caída.\nFlechas izquierda/derecha: mueven la pieza.\nM: mutea la música.\nP: da play a la música.\nNúmeros 1, 2 y 3: seleccionan canción.
			""")

def jugar():
	
	global nombreJugador, avatarJugador

	if variableNombre.get()!="":
		nombreJugador=variableNombre.get()

	if varOpcion.get()==1:
		avatarJugador="2.jpg"

	elif varOpcion.get()==2:
		avatarJugador="3.jpg"

	elif varOpcion.get()==3:
		avatarJugador="4.jpg"


	root.destroy()





#----------------raiz-----------------------------

root=Tk()
root.config(bg="white")
root.title("Tetris en red")
root.iconbitmap("icono.ico")
root.resizable(0,0)

#variables globales

variableNombre=StringVar()
nombreJugador="Player"
varOpcion=IntVar()
avatarJugador="1.jpg"
listaMusica=["1.wmv","2.wmv","3.wmv"]
track=0

#--------------------------frame usuario---------------------------------

frameNombre=Frame(root,width=400,height=30,relief="raised")
frameNombre.grid(columnspan=4)
frameNombre.grid_propagate(False)

cuadroNombre=Entry(frameNombre,textvariable=variableNombre)
cuadroNombre.grid(row=0,column=1,padx=25,pady=10)
nombreLabel=Label(frameNombre,text="Nombre:")
nombreLabel.grid(row=0,column=0,padx=50,pady=10)

#botonAceptar=Button(frameNombre,text="Aceptar",command=aceptarNombre)
#botonAceptar.grid(row=0,column=2,padx=10,pady=10)

#----------------------frame opciones avatar-----------------------------

frameAvatar=Frame(root,width=400,height=60,relief="raised")
frameAvatar.grid(columnspan=4)
frameAvatar.grid_propagate(False)

avatarLabel=Label(frameAvatar,text="Escoge tu avatar:")
avatarLabel.grid(row=1,column=0,padx=10,pady=5)


Radiobutton(frameAvatar, value=0,variable=varOpcion,text="Opción 1").grid(row=2,column=0,pady=5)
Radiobutton(frameAvatar, value=1,variable=varOpcion,text="Opción 2").grid(row=2,column=1,padx=10,pady=5)
Radiobutton(frameAvatar, value=2,variable=varOpcion,text="Opción 3").grid(row=2,column=2,padx=10,pady=5)
Radiobutton(frameAvatar, value=3,variable=varOpcion,text="Opción 4").grid(row=2,column=3,padx=10,pady=5)

#----------------------------frame imagenes---------------------------------

frameImagenes=Frame(root,width=400,height=100,relief="raised")
frameImagenes.grid(columnspan=4)
frameImagenes.grid_propagate(False)

imagen1=PhotoImage(file="1.jpg")
imagen2=PhotoImage(file="2.jpg")
imagen3=PhotoImage(file="3.jpg")
imagen4=PhotoImage(file="4.jpg")

Label(frameImagenes,image=imagen1).grid(row=0,column=0,padx=20,pady=10)
Label(frameImagenes,image=imagen2).grid(row=0,column=1,padx=20,pady=10)
Label(frameImagenes,image=imagen3).grid(row=0,column=2,padx=20,pady=10)
Label(frameImagenes,image=imagen4).grid(row=0,column=3,padx=20,pady=10)

#-------------------------------frame play buttom---------------------------
frameBotones=Frame(root,width=400,height=65)
frameBotones.grid()
frameBotones.grid_propagate(False)

BotonPlay=Button(frameBotones,command=jugar,text="JUGAR!",fg="orange",bd=10,relief="raised",bg="blue",activebackground="yellow",activeforeground="green",width=10,font=("Comic Sans MS",16))
BotonPlay.place(x=125)

BotonSalir=Button(frameBotones,command=salirJuego,text="Salir",bd=5,relief="sunken",bg="white",activebackground="red",fg="red",activeforeground="white",font=("Comic Sans MS",10),width=4)
BotonSalir.place(x=335,y=20)

#--------------------------barra de menu-----------------------------------

barraMenu=Menu(root)
root.config(menu=barraMenu)
archivoMenu=Menu(barraMenu,tearoff=0)
archivoMenu.add_command(label="Instrucciones",command=instrucciones)
archivoMenu.add_command(label="Controles",command=controles)
archivoMenu.add_command(label="Acerca de",command=infoTetris)
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir",command=salirJuego)


barraMenu.add_cascade(label="Menu",menu=archivoMenu)
#--------------------------------------------------------------------------

root.mainloop()

#-----------------------ventana pygame---------------------------------
def dibujarVentana():
	
	global avatarJugador, nombreJugador

	rectangulo=pygame.Rect(0,0,100,100)
	pygame.draw.rect(ventana,(200,0,0),rectangulo,5)
	rectangulo=pygame.Rect(0,100,100,100)
	pygame.draw.rect(ventana,(200,0,0),rectangulo,5)
	rectangulo=pygame.Rect(0,200,100,67)
	pygame.draw.rect(ventana,(200,0,0),rectangulo,5)
	rectangulo=pygame.Rect(0,267,100,67)
	pygame.draw.rect(ventana,(200,0,0),rectangulo,5)
	rectangulo=pygame.Rect(0,334,100,66)
	pygame.draw.rect(ventana,(200,0,0),rectangulo,5)
	rectangulo=pygame.Rect(100,0,200,400)
	pygame.draw.rect(ventana,(200,0,0),rectangulo,7)


	Avatar=pygame.image.load(avatarJugador)
	ventana.blit(Avatar,(20,30))

	miFuente=pygame.font.SysFont("Century Gothic",20)
	nombre=miFuente.render(nombreJugador,0,(0,0,200))
	ventana.blit(nombre,(20,3))
	
	level=miFuente.render("Level",0,(0,200,200))
	ventana.blit(level,(20,200))
	
	score=miFuente.render("Score",0,(0,200,200))
	ventana.blit(score,(20,267))

	lines=miFuente.render("Lines",0,(0,200,200))
	ventana.blit(lines,(20,334))

ancho=300
alto=400
velocidad=5

pygame.init()

ventana = pygame.display.set_mode((ancho,alto))
icon=pygame.image.load("icono2.ico")
pygame.display.set_icon(icon)
pygame.display.set_caption("Tetris en red")

reloj = pygame.time.Clock()	

fuente=pygame.font.SysFont("Century",50)

def TetrisEnRed():

	pygame.mixer.music.load("1.wmv")
	pygame.mixer.music.play(5)
	
	while True:

		reloj.tick(60)		
		Tiempo = pygame.time.get_ticks()/1000


		ventana.fill((255,255,255))
		
		if 0<Tiempo<1:
			contador=fuente.render("3...",0,(70,240,0))
			ventana.blit(contador,(120,150))

		if 1<Tiempo<2:
			contador=fuente.render("2...",0,(0,70,240))
			ventana.blit(contador,(120,150))

		if 2<Tiempo<3:
			contador=fuente.render("1...",0,(240,70,0))
			ventana.blit(contador,(120,150))	
		
		if Tiempo>3:
			dibujarVentana()	


		for event in pygame.event.get():

			if event.type==pygame.KEYDOWN:
				if event.key==K_m:
					pygame.mixer.music.stop()

				elif event.key==K_p:
					pygame.mixer.music.play(5)

				elif event.key==K_1:
					pygame.mixer.music.load("1.wmv")
					pygame.mixer.music.play(5)

				elif event.key==K_2:
					pygame.mixer.music.load("2.wmv")
					pygame.mixer.music.play(5)

				elif event.key==K_3:
					pygame.mixer.music.load("3.wmv")
					pygame.mixer.music.play(5)

				"""elif event.key==K_ESCAPE:
						salirJuego()"""

			if event.type == QUIT:
				pygame.quit()
				sys.exit()			

		
		pygame.display.update()

TetrisEnRed()




