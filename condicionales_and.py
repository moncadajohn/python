distancia = int(input("Ingrese la distancia : "))
hermanos = int(input("Cuántos hermanos tienes en el centro : "))
sueldo = int(input("Cuál es el salario? : "))

#if distancia>40 and hermanos>2  and sueldo<=20000:
if distancia>40 and hermanos>2  or sueldo<=20000: #utilizando or
	print("** Tienes derecho a beca **")
else:
	print("!! No tienes derecho a beca !!")