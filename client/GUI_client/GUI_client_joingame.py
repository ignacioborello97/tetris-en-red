from tkinter import *
from tkinter import messagebox

def volver():
	
	valor=messagebox.askquestion("Volver","Deseas volver al menu principal?")

	if valor=="yes":
		root.destroy()
        #acá funcion main_menu

	if valor=="no":
		pass

def unirse():
	
	global codigoPartida

	if variablePartida.get()!="":
		codigoPartida=variablePartida.get()
    #aca funcion para conectarse
	root.destroy()

root=Tk()
root.config(bg="white")
root.title("Unirse a partida - Tetris en red")
root.iconbitmap("icono2.ico")
root.resizable(0,0)

variablePartida=StringVar()
codigoPartida=""

#--------------------------frame usuario---------------------------------
frameNombre=Frame(root,width=400,height=60,relief="raised")
frameNombre.grid(columnspan=4)
frameNombre.grid_propagate(False)

cuadroNombre=Entry(frameNombre,textvariable=variablePartida)
cuadroNombre.grid(row=0,column=1,padx=25,pady=10)
nombreLabel=Label(frameNombre,text="Codigo:")
nombreLabel.grid(row=0,column=0,padx=50,pady=10)

#-------------------------------frame play button---------------------------
frameBotones=Frame(root,width=400,height=60)
frameBotones.grid()
frameBotones.grid_propagate(False)

BotonPlay=Button(frameBotones,command=unirse,text="Unirse",fg="yellow",bd=10,relief="raised",bg="blue",activebackground="yellow",activeforeground="blue",width=10,font=("Comic Sans MS",12))
BotonPlay.place(x=125)

BotonVolver=Button(frameBotones,command=volver,text="Volver",bd=5,relief="raised",bg="grey",activebackground="red",fg="black",activeforeground="white",font=("Comic Sans MS",10),width=4)
BotonVolver.place(x=335,y=20)

root.mainloop()