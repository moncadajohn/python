#METACARACTERES - CARACTERES COMODÍN
#Anclas y clases de caracteres

import re


lista_nombres=['Ana',
               'Pedro',
               'María',
               'Rosa',
               'Sandra',
               'Celia']

for elemento in lista_nombres:
	#if re.findall('^San', elemento): #los que inician por
	if re.findall('[o-t]', elemento):#rango de datos 
	   print(elemento)

print("****************************")

lista_nombres=['Ma1',
               'Se1',
               'Ma2',
               'Ba1',
               'Ma3',
               'Va1',
               'Va2',
               'Ma4']

for elemento in lista_nombres:
	#if re.findall('Ma[0-3]', elemento):#Buscar los Ma del 0 al 3
	if re.findall('Ma[^0-3]', elemento):#Buscar los diferentes a  Ma del 0 al 3 
	   print(elemento)

print("****************************")

lista_nombres=['Ma1',
               'Se1',
               'Ma2',
               'Ba1',
               'Ma3',
               'Ma:3',
               'Va1',
               'Va2',
               'Ma4',
               'MaA',
               'MaB',
               'MaC',
               'Ma.5',
               'Ma:C']

for elemento in lista_nombres:
	#if re.findall('Ma[0-3]', elemento):#Buscar los Ma del 0 al 3
	#if re.findall('Ma[^0-3]', elemento):#Buscar los diferentes a  Ma del 0 al 3
	#if re.findall('Ma[0-3A-B]', elemento):#Buscar los ma del 0 al 3 y del A al B
	if re.findall('Ma[.:]', elemento):#Buscar los que tengan esos puntos
	   print(elemento)