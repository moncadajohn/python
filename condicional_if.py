ingresanota = int(input("Ingresa la nota del alumno"))

def evaluacion(nota):
	valoracion = "Aprobado"
	if nota <5:
		valoracion="No Aprobado"
	return valoracion

print(evaluacion(ingresanota))