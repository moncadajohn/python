import sqlite3

#Abrir - crear conexíón
miConexion=sqlite3.connect("GestionProductos")

#Crear cursor o puntero
miCursor=miConexion.cursor()

miCursor.execute('''
	CREATE TABLE PRODUCTOS(
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
	PRECIO INTEGER,
	SECCION VARCHAR(20))
	''')

#creación de lista para llenar la tabla
productos=[
   ("pelota",20,"xuguetería"),
   ("pantalón",15,"confección"),
   ("destornillador",25,"ferretería"),
   ("xarrón",45,"cerámica"),
   ("pantalones",35,"confección"),
]
#executar la sentencia escrita anteriormente
miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)",productos)

#confirmar cambios
miConexion.commit()

#Cerrar conexión
miConexion.close()


