from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("MENUBAR")

#función para crear ventana emergente
def infoAdicional():
	messagebox.showinfo("Procesador de leidy", "Procesador de textos versión 2019")


def avisoDocumentacion():
	messagebox.showwarning("Documentación","Toda la Documentación está disponible")

def salirAplicacion():
	valor=messagebox.askokcancel("Salir", "¿Deseas salir de la aplicación?")
	if valor:
		root.destroy()

def cerrarDocumento():
	valor=messagebox.askretrycancel("Reintentar", "Documento bloqueado")
	if valor=="False":
		root.destroy()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu,tearoff=0)
#elementos
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)


archivoEdicion=Menu(barraMenu,tearoff=0)
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu,tearoff=0)
archivoHerramientas.add_command(label="Compilar")
archivoHerramientas.add_command(label="Verificar")
archivoHerramientas.add_command(label="Analizar")

archivoAyuda=Menu(barraMenu,tearoff=0)
archivoAyuda.add_command(label="Documentación", command=avisoDocumentacion)
archivoAyuda.add_command(label="Acerca de...", command=infoAdicional)


barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edición", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)


root.mainloop()