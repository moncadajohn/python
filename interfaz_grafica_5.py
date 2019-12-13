from tkinter import *

#construir la raiz

root=Tk()
root.title("Text Box")
miFrame=Frame(root,width=500,height=400)
miFrame.pack()

minombre=StringVar()

cuadroTexto=Entry(miFrame,textvariable=minombre)
cuadroTexto.grid(row=0,column=1,padx=20,pady=4)
cuadroTexto.config(fg="red",justify="center")

cuadroPassword=Entry(miFrame)
cuadroPassword.grid(row=1,column=1,padx=20,pady=4)
cuadroPassword.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2,column=1,padx=4,pady=4)

cuadroComentarios=Text(miFrame,width=15, height=5)
cuadroComentarios.grid(row=4,column=1,padx=4,pady=4)

#crear barra de desplazamiento
scrollVert=Scrollbar(miFrame,command=cuadroComentarios.yview)
scrollVert.grid(row=4,column=2, sticky="nsew")

cuadroComentarios.config(yscrollcommand=scrollVert.set) 


cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3,column=1,padx=4,pady=4)

nombreLabel=Label(miFrame,text="Nombre: ")
nombreLabel.grid(row=0,column=0,sticky="w",padx=4,pady=4)

passwordLabel=Label(miFrame,text="Password: ")
passwordLabel.grid(row=1,column=0,sticky="w",padx=4,pady=4)

apellidoLabel=Label(miFrame,text="Apellido: ")
apellidoLabel.grid(row=2,column=0,sticky="w",padx=4,pady=4)

direccionLabel=Label(miFrame,text="Dirección: ")
direccionLabel.grid(row=3,column=0,sticky="w",padx=4,pady=4)

comentariosLabel=Label(miFrame,text="Comentarios: ")
comentariosLabel.grid(row=4,column=0,sticky="w",padx=4,pady=4)

def codigoBoton():
	minombre.set("Ohn Moncada Velásquez")

botonEnvio=Button(root, text="Enviar",command=codigoBoton)
botonEnvio.pack()

root.mainloop()