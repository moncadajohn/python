from tkinter import *

#construir la raiz

raiz=Tk()
raiz.title("Probando ventana!!")
raiz.resizable(True,True) #redimensionar a lo ancho y a lo alto
raiz.iconbitmap("imagenes/favicon.ico")
raiz.geometry("650x350")#tamaño personalido de ventanas ancho x alto
raiz.config(bg="gray")#cambiar el color de fondo bg de background
raiz.mainloop()
