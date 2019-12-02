mitupla=("uan",13,1,1995)#las tuplas normalmente vien con paréntesis aunque no es obligatorio

milista=list(mitupla)#convertir una tupla en una lista
print(mitupla)
print(milista)
print(mitupla[2])

#convertir una lista  en una tupla
milista2=["locked",14,1,1995,14]
mitupla2=tuple(milista2)#con tuple es que se convierte a tupla
print(mitupla2)

print("locked" in mitupla2)#buscar si existe el elemento en la tupla

#averiguar cuántas veces se encuentra un elementos x en la tupla
print("el elemento se encuentra",mitupla2.count(14),"veces")

#averiguar la longitud de una tupla
print("la tupla contiene ",len(mitupla2),"elementos")

#tupla unitaria
mitupla3=("Moncada",)#necesita la coma

#puedo crear tuplas sin paréntesis
mitupla4="velásquez",1980,30,6
print(mitupla4)

#asignar elementos de una tupla a variables/
#desempaquetado de tuplas
mitupla5="velásquez",1980,30,6
apellido, year, day, month=mitupla5
print("Apellido :",apellido)
print("Año :",year)
print("Mes :",month)
print("Día :",day)


