while True:
    try:
         numero_uno = int(input("numero_uno : "))
         numero_dos = int(input("numero_dos : "))
         break
    except ValueError:
    	print("Los valores deben ser numéricos")

def pares(a,b):
    if numero_uno%2==0 and numero_dos%2==0:
       print("ambos números son pares")
       
    elif numero_uno%2!=0 and numero_dos%2!=0:
            print("Ningún número es par")

    elif numero_uno%2==0 and numero_dos%2!=0:
             print("el número",numero_uno,"es par")
    elif numero_uno%2!=0 and numero_dos%2==0:
             print("el número",numero_dos,"es par")

pares(numero_uno,numero_dos)