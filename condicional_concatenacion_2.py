salario_presidente = int(input("Salario Presidente : "))
print("Salario : ",salario_presidente)

salario_director = int(input("Salario Director : "))
print("Salario : ",salario_director)

salario_boss = int(input("Salario Boss : "))
print("Salario : ",salario_boss)

salario_administrativo = int(input("Salario Administrativo : "))
print("Salario : ",salario_administrativo)

if salario_administrativo<salario_boss<salario_director<salario_presidente:
	print("El orden de salarios es correcto")
else:
	print("Algo no está correcto")
