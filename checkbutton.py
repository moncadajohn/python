from tkinter import *

root=Tk()
root.title("checkbutton")


##creación de las variables para los check, activo vale 1 e inactivo 0

playa=IntVar()
montagna=IntVar()
turismoRural=IntVar()

def opcionesviae():
	opcionEscogida=""

	if(playa.get()==1):
		opcionEscogida+=" Playa"

	if(montagna.get()==1):
		opcionEscogida+=" Montaña"

	if(turismoRural.get()==1):
		opcionEscogida+=" Turismo Rural"

	textoFinal.config(text=opcionEscogida)


foto=PhotoImage(file="imagenes/numero10.png")
Label(root,image=foto).pack()

frame = Frame(root).pack()

Label(frame,text="elige destinos", width=50).pack()


Checkbutton(frame,text="Playa",variable=playa, onvalue=1, offvalue=0,command=opcionesviae).pack()
Checkbutton(frame,text="Montaña",variable=montagna, onvalue=1, offvalue=0,command=opcionesviae).pack()
Checkbutton(frame,text="Turismo rural",variable=turismoRural, onvalue=1, offvalue=0,command=opcionesviae).pack()




textoFinal=Label(frame)
textoFinal.pack()


root.mainloop()