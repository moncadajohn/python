for i in[1,2,3]:
	print("saludo")
print("******")
#muestra la cantidad de elementos que tenga la lista
for i in["casa","carro","beca","burro"]:
	print(i)
print("******")
#mostrar los datos de forma horizontal
for i in[1,2,3]:
	print("saludo",end=", ")

print("******")
#Recorriendo string de caracteres
for i in "moncadavelasquez.com":
	print("$")

#Revisemos un caso de eemplo

contador = 0
correo = input("Ingresa tu email : ")

for i in correo:
	if(i == "@" or i=="."):
		contador = contador+1

if contador == 2:
	print("El email es correcto")
else:
	print("El email no es correcto")

