#FUNCIÓN FILTER: 
#verifica que los elementos de una secuencia cumplen una condición,
#devolvendo un iterador con los elementos que cumplen dicha condición.

"""def numero_par(num):
	if num % 2 == 0:
	   return True"""

numeros=[17,24,7,38,52,92,15,4]

print(list(filter(lambda numero_par:numero_par%2==0, numeros)))