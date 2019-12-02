from io import open

#escribir y leer archivos

#ESCRIBIR
"""
archivo_texto=open("archivo.txt","w") # w de write
frase= "Estupendo día para estudiar python \n el miércoles"

archivo_texto.write(frase)
archivo_texto.close()
"""

#LEER
"""
archivo_texto=open("archivo.txt","r") # r de read

texto=archivo_texto.read()
print(texto)
archivo_texto.close()

##LEER LA INFORMACIÓN Y GUARDARLA EN UNA LISTA
"""
"""
archivo_texto=open("archivo.txt","r")
lineas_texto=archivo_texto.readlines()
print(lineas_texto[0])
archivo_texto.close()
"""

#AGREGAR MÁS LÍNEAS DE TEXTO
archivo_texto=open("archivo.txt","a") # a de append
archivo_texto.write("\nsiempre es una buena ocasión para estudiar python")
archivo_texto.close()