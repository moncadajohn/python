while True:
       try:
           letra = int(input("ingresa un número: "))
           otra_letra = int(input("ingresa otro número: "))
           print("los valores ingresados fueron: "+str(letra)+"y"+str(otra_letra))
           break
       except ValueError:
	       print("Los valores a ingresar deben ser numéricos")


