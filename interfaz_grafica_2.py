from tkinter import *

#construir la raiz

raiz=Tk()
raiz.title("Probando ventana!!")
#raiz.resizable(True,True) #redimensionar a lo ancho y a lo alto
raiz.iconbitmap("imagenes/favicon.ico")
#raiz.geometry("650x350")#tamaño personalido de ventanas ancho x alto
raiz.config(bg="gray")#cambiar el color de fondo bg de background

#crear un frame
miFrame=Frame()
#miFrame.pack()#con esto lo que se hace es empaquetarlo para que haga parte de la raíz, de otra forma es como si quedara por fuera
miFrame.pack(fill="both", expand="True") #relleno el resto de la raíz con el frame
miFrame.config(bg="cyan")
miFrame.config(width="650", height="350")
miFrame.config(bd="18")#tamaño del borde del frame
miFrame.config(relief="groove")#cambiar borde del frame
miFrame.config(cursor="hand2")#cmbiar el cursor
raiz.mainloop()
