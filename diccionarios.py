midiccionario={"Alemania":"Berlín","Francia":"París","Reino Unido":"Londres","Colombia":"Bogotá"}

#ver la clave valor
print(midiccionario["Colombia"])

#ver diccionario entero
print(midiccionario)

#Agregar elementos al diccionario
midiccionario["Italia"]="Lisboa"
print(midiccionario)

#corregir un valor del diccionario
midiccionario["Italia"]="Roma"
print(midiccionario)

#Eliminar clave valor
del midiccionario["Reino Unido"]
print(midiccionario)

#diferentes tipos de elementos en el diccionario
midiccionario2={"Alemania":"Berlín",10:"Messi","Falcao":9}
print(midiccionario2)

#Agregar un valor a cada clave del diccionario 
mitupla=("España","Colombia","Francia","Noruega")
midiccionario3 = {mitupla[0]:"Madrid",mitupla[1]:"Bogotá",mitupla[2]:"París",mitupla[3]:"Oslo"}
print(midiccionario3)

#Diccionario que almacena una tupla
midiccionario4 ={23:"ordan","Nombre":"Michael","Equipo":"Chicago Bulls","Anillos":[1991,1992,1993,1996,1997,1998]}
print(midiccionario4)

#Crear un diccionario dentro de otro diccionario
midiccionario5 ={23:"ordan","Nombre":"Michael","Equipo":"Chicago Bulls","Anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midiccionario5)
print(midiccionario5["Anillos"])

#Mostrar únicamente las claves
print(midiccionario5.keys())
#Mostrar únicamente los valores
print(midiccionario5.values())
#Longitud del diccionario
print(len(midiccionario5))

