import math
print("programa de raíz cuadrada")

numero = int(input("Ingresa un número para calcular raíz cuadrada : "))

intentos = 0

while numero<0:
	print("no se puede hallar la raíz de un número negativo")
	if intentos ==2:
	   print("Haz consumido los intentos permitidos")
	   break
	numero = int(input("Ingresa un número para calcular raíz cuadrada : "))
	if numero<0:
		intentos= intentos+1

if intentos<2:
   solucion = int(math.sqrt(numero))
   print("La solucion de la raiz cuadrada de",numero,"es :"+str(solucion))

