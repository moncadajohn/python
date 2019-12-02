#utilización del continue
for letra in "Python":
	if letra ==" ":
	   continue
	print("Viendo la letra: "+letra)



nombre = "moncada velasquez"
contador = 0
for i in nombre:
    if i ==" ":
       continue
    contador+=1
print("La palabra ",nombre, "tiene",contador)

##utilización de pass
class MiClase:
	pass
	#permite que la clase quede en estand by y el sistema continúe

#Utilización de Else

email=input("introducir correo")
for i in email:
    if i=="@":
    	arroba=True
    	break;
else:
	arroba=False
print(arroba)



