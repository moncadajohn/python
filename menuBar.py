from tkinter import *

root=Tk()
root.title("MENUBAR")

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu,tearoff=0)
#elementos
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")


archivoEdicion=Menu(barraMenu,tearoff=0)
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu,tearoff=0)
archivoHerramientas.add_command(label="Compilar")
archivoHerramientas.add_command(label="Verificar")
archivoHerramientas.add_command(label="Analizar")

archivoAyuda=Menu(barraMenu,tearoff=0)
archivoAyuda.add_command(label="Documentación")
archivoAyuda.add_command(label="Redes Sociales")


barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edición", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)


root.mainloop()