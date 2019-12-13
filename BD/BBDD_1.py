import sqlite3

#Abrir - crear conexíón
miConexion=sqlite3.connect("PrimeraBD")

#Crear cursor o puntero
miCursor=miConexion.cursor()
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER,SECCION VARCHAR(20))")
miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN',15,'DEPORTES')")
miConexion.commit()




#Cerrar conexión
miConexion.close()


