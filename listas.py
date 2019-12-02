miLista=["maria",5,True,78.35,"pepino"]
miLista.append("moncada")#agregar un nuevo elemento a la lista en el final
miLista.insert(2,"leidy")#agregar un elemento a la lista definiendo su posición
miLista.extend(["lucía","ana","angelina"])#agregar más elementos a la lista
miLista.remove("ana")#eliminar un elemento de la lista
miLista.pop() #elimina el último elemento de la lista


print(miLista[:]) #consultar toda la lista
print(miLista[1]) #consultar un solo elemento
print(miLista[-4]) #consultar de atrás para adelante, inicia en -1
print(miLista[1:3])#consultar por porciones de lista
print(miLista[2:])#consultar desde el índice 2 los elementos siguientes
print(miLista.index("leidy"))#conocer el índice de algún elemento
print("pepe"in miLista)#conocer si existe el elemento en la lista


"""sumar dos listas"""
milista2=["carlos",4,5.65]
milista3=["falcao","rodriguez",10]
miLista4 = milista2+milista3
print(miLista4[:])

miLista5=["went","alerta",56] *3 #modo repetidor
print(miLista5[:])