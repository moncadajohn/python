from io import open

#archivo_texto=open("archivo.txt","r") # a de append
#archivo_texto.write("\nsiempre es una buena ocasión para estudiar python")
"""
archivo_texto.seek(10)
print(archivo_texto.read())

archivo_texto.seek(0)
print(archivo_texto.read(11)) ##con esta opción nos permite leer hasta determinada posición

archivo_texto.close()

#método seek() permite enviarle un parámetro para ubicar el puntero(cursor) en el archivo
"""
##podemos también posicionar el cursor en la mitad del texto del archivo
"""
archivo_texto.seek(len(archivo_texto.read())/2)
print(archivo_texto.read())
"""
##ubicarnos al final de la primer línea para que empiece a leer
"""
archivo_texto.seek(len(archivo_texto.readline()))
print(archivo_texto.read())
"""
##permitir que el archivo pueda ser de lectura y escritura
archivo_texto=open("archivo.txt","r+")#lectura y escritura
##archivo_texto.write("Comienzo del Texto")
#print(archivo_texto.readlines())
lista_texto=archivo_texto.readlines()
lista_texto[1]="Línea incluída desde el exterior\n"

archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)
archivo_texto.close()





