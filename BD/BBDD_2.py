import sqlite3

#Abrir - crear conexíón
miConexion=sqlite3.connect("PrimeraBD")

#Crear cursor o puntero
miCursor=miConexion.cursor()
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER,SECCION VARCHAR(20))")
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN',15,'DEPORTES')")
#crear varios productos
"""
variosProductos=[
      ("Camiseta",10,"Deportes"),
      ("Xarrón",90,"Cerámica"),
      ("Camión",20,"xuguetería")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",variosProductos)
"""
#consultar la información ingresada
miCursor.execute("SELECT * FROM PRODUCTOS")
consulta=miCursor.fetchall()#devuelve una lista con todos los registros

#primera forma
#print(consulta)

#segunda forma
#for producto in consulta:
#    print(producto)

#tercera forma
for producto in consulta:
    print("Nombre Artículo: ",producto[0], "Sección: ",producto[2])

miConexion.commit()

#Cerrar conexión
miConexion.close()


