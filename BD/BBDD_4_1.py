import sqlite3

#Abrir - crear conexíón
miConexion=sqlite3.connect("GestionProductos")

#Crear cursor o puntero
miCursor=miConexion.cursor()

"""
#SELECT Ó R DEL CRUD
miCursor.execute("SELECT * FROM PRODUCTOS WHERE ID=2")

productos=miCursor.fetchall()
for p in productos:
  print(productos)

"""
"""
#UPDATE Ó U DEL CRUD
miCursor.execute("UPDATE PRODUCTOS SET PRECIO=100 WHERE ID=2")

"""
#DELETE Ó D DEL CRUD
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")
#confirmar cambios
miConexion.commit()

#Cerrar conexión
miConexion.close()


