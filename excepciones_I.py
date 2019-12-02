def suma(a,b):
	return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):

    try:
        return a/b

    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return "Operación Erronea"

numero_uno = int(input("introduce el primer número : "))
numero_dos = int(input("introduce el segundo número : "))
operacion = input("introduce la opción a realizar : suma, resta, multiplica, divide : ")


if operacion =="suma":
   print(suma(numero_uno,numero_dos))
elif operacion == "resta":
	print(resta(numero_uno,numero_dos))
elif operacion == "multiplica":
	print(multiplicacion(numero_uno,numero_dos))
elif operacion == "divide":
	print(division(numero_uno,numero_dos))
else:
	print("Operación no encontrada")
print("Finaliza programa ")



