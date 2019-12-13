import re

nombre1="sandra lópez"
nombre2="Antonio lópez"
nombre3="María lópez"

#if re.match("Sandra", nombre3, re.IGNORECASE):#Buscar por nombre y con ignorecase no importa si es mayúscula o minúscula
if re.match(".ar", nombre3, re.IGNORECASE):#Busca lo que inicie con ara
	print("Hemos encontrado el nombre")
else:
	print("No Hemos encontrado el nombre")

print("***********otro example**************")

cadena1="sandra lópez"
cadena2="546474747"
cadena3="a5678978"

if re.match("\d", cadena2, re.IGNORECASE):#Busca lo que inicie con ara
	print("Hemos encontrado el número")
else:
	print("No Hemos encontrado el número")



print("********UTILIZACIÓN DE SEARCH********************")

nombre1="sandra lópez"
nombre2="Antonio gómez"
nombre3="María lópez"
nombre4="asdfhasd71slasdlfadslf"

#if re.search("lópez", nombre1, re.IGNORECASE):#Busca lo que inicie con ara
if re.search("71", nombre4, re.IGNORECASE):#Buscar el 71
	print("Hemos encontrado el nombre")
else:
	print("No Hemos encontrado el nombre")
