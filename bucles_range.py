for i in range(5, 50, 3): #significa : inicie en 5 hasta el 49 y cuente de 3 en 3
	print("el valor de variable",{i})



##caso 2

valido = False

email = input("ingresa correo electrónico : ")

for i in range(len(email)):
	if email[i]=="@":
         valido = True

if valido:
	print("email con arroba, puede ser correcto")

else:
	print("El email no contiene arroba, por lo tanto es incorrecto")



