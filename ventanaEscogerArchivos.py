from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root=Tk()
root.title("VENTADA DIALOGO")

#función para abrir el fichero
def abreFichero():
	fichero=filedialog.askopenfilename(title="Abrir", filetypes=(("Archivos de Excel","*.xlsx"),
		                                                        ("Archivos de Texto","*.txt"),
		                                                        ("Todos los Archivos","*.*")))
	print(fichero)#devolverá la ruta del fichero que queremos abrir

Button(root,text="Abrir Fichero", command=abreFichero).pack()





root.mainloop()