#METACARACTERES - CARACTERES COMODÍN
#Anclas y clases de caracteres

import re


lista_nombres=['Ana Gómez',
               'María Martín',
               'Sandra López',
               'Santiago Martín']

for elemento in lista_nombres:
	#if re.findall('^San', elemento): #los que inician por
	if re.findall('Martín$', elemento):#los que terminan en 
	   print(elemento)


print("****************otro caso exemplo*************")

#otro exemplo para usar

lista_nombres2=['Ana Gómez',
               'María Martín',
               'Sandra López',
               'pepito el ñato',
               'Santiago Martín']

for elemento2 in lista_nombres2:
	if re.findall('[ñ]', elemento2):
		print(elemento2)

print("****************otro caso exemplo*************")

#otro exemplo para usar

lista_nombres2=['muxeres',
               'hombres',
               'niños',
               'mascotas',
               'niñas']

for elemento2 in lista_nombres2:
	if re.findall('niñ[oa]s', elemento2):
		print(elemento2)