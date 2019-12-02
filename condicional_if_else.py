edad = int(input("Ingresa tu edad : "))

def valida_Edad(valor):
	
	if valor < 18:
	   mostrar = "Eres Menor de Edad, No puedes pasar"
	elif valor >=100:
    	 mostrar = "Edad Muy alta"
	else:
		 mostrar = "Eres Mayor de Edad, puedes pasar"
	
	return mostrar

print(valida_Edad(edad))
print("Programa Terminado")
