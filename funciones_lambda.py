#función normal
"""def areaTriangulo(base, altura):
	return (base*altura)/2

triangulo1=areaTriangulo(5,7)
triangulo2=areaTriangulo(8,4)

print(triangulo1)
print(triangulo2)"""

#Utilizando lambda
areaTriangulo=lambda base,altura:(base*altura)/2
triangulo1=areaTriangulo(7,5)
triangulo2=areaTriangulo(8,4)

print(triangulo1)
print(triangulo2)
print("(;)(;)(;)(;)(;)(;)(;)(;)(;)(;)(;)(;)()()()()()()()")
##otro exemplo

al_cubo=lambda numero:numero**3
print(al_cubo(13))

print("(;)(;)(;)(;)(;)(;)(;)(;)(;)(;)(;)(;)()()()()()()()")

al_cubo=lambda numero:pow(numero,3)
print(al_cubo(13))

print("*********************************************")
destacar_valor=lambda comision:"¡{}! $".format(comision)
comision_ana=15467
print(destacar_valor(comision_ana))
