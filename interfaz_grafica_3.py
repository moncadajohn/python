from tkinter import *

#construir la raiz

root=Tk()
root.title("New Window")

miFrame=Frame(root,width=500, height=400)
miFrame.pack()
miImagen=PhotoImage(file="imagenes/clock.gif")
#miLabel=Label(miFrame, text="Saludos desde el Label", fg="red",font=("Comic Sans Ms",18))
Label(miFrame,image=miImagen).place(x=20,y=0)
#miLabel.place(x=0, y=0)#ubicación del label
root.mainloop()