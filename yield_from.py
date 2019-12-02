def devuelve_ciudades(*ciudades): #*significa que es un número indeterminado de elementos, si es uno o más además los recibirá en forma de tupla
    for elemento in ciudades:
    	#for subElemento in elemento:
    	    #yield subElemento
    	    yield from elemento  ##funciona como un bucle for anidado
ciudades_devueltas=devuelve_ciudades("madrid","barcelona","vilbao","vizcaya")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))