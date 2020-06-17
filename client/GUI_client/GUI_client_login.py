from tkinter import *
from tkinter import messagebox
#from GUI_client_mainmenu import main_menu

root=Tk()
root.config(bg="white")
root.title("Tetris en red")
root.iconbitmap('icono2.ico')
root.resizable(0,0)

variableNombre=StringVar()
nombreJugador="Player"
varOpcion=IntVar()
avatarJugador=''

imagen1=PhotoImage(file=avatarJugador)
imagen2=PhotoImage(file='')
imagen3=PhotoImage(file='')
imagen4=PhotoImage(file='')

def salirJuego():
	
	valor=messagebox.askquestion('Salir','Deseas salir de la aplicacion?')

	if valor=='yes':
		root.destroy()

	if valor=='no':
		pass

def jugar():
	
	global nombreJugador, avatarJugador

	if variableNombre.get()!='':
		nombreJugador=variableNombre.get()

	if varOpcion.get()==1:
		avatarJugador=''

	elif varOpcion.get()==2:
		avatarJugador=''

	elif varOpcion.get()==3:
		avatarJugador=''

	root.destroy()
	

#--------------------------frame usuario---------------------------------
frameNombre=Frame(root,width=400,height=30,relief="raised")
frameNombre.grid(columnspan=4)
frameNombre.grid_propagate(False)

cuadroNombre=Entry(frameNombre,textvariable=variableNombre)
cuadroNombre.grid(row=0,column=1,padx=25,pady=10)
nombreLabel=Label(frameNombre,text="Nombre:")
nombreLabel.grid(row=0,column=0,padx=50,pady=10)

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

Label(frameImagenes,image=imagen1).grid(row=0,column=0,padx=20,pady=10)
Label(frameImagenes,image=imagen2).grid(row=0,column=1,padx=20,pady=10)
Label(frameImagenes,image=imagen3).grid(row=0,column=2,padx=20,pady=10)
Label(frameImagenes,image=imagen4).grid(row=0,column=3,padx=20,pady=10)

#-------------------------------frame play button---------------------------
frameBotones=Frame(root,width=400,height=65)
frameBotones.grid()
frameBotones.grid_propagate(False)

BotonPlay=Button(frameBotones,command=jugar,text="Log In",fg="yellow",bd=10,relief="raised",bg="blue",activebackground="yellow",activeforeground="blue",width=10,font=("Comic Sans MS",16))
BotonPlay.place(x=125)

BotonSalir=Button(frameBotones,command=salirJuego,text="Salir",bd=5,relief="raised",bg="grey",activebackground="red",fg="black",activeforeground="white",font=("Comic Sans MS",10),width=4)
BotonSalir.place(x=335,y=20)

root.mainloop()