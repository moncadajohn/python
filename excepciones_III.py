import math
"""def evaluaEdad(edad):
    if edad<0:
    	raise typeError("No se permiten edades negativas")##está saliendo error
    if edad<20:
        return "you are very young"
    elif edad<40:
         return "you are young"
    elif edad<65:
         return "eres maduro"
    elif edad<100:
         return "cuidate"
print(evaluaEdad(-1))"""
##con raise creamos nuestras propias excepciones
#en este eemplo se le cambia el valor a ValueError

def calcularaiz(num1):
           if num1<0:
                raise ValueError("El número no puede ser negativo")
           else:
           	   return math.sqrt(num1)
op1 = int(input("ingresa un número :"))
try:
    print(calcularaiz(op1))
except ValueError as ErrordeNumeroNegativo:
    print(ErrordeNumeroNegativo)
print("programa terminado")