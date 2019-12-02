def divide():
    try:
        op1=(float(input("Ingresa primer número: ")))
        op2=(float(input("Ingresa segundo número: ")))
        print("El resultado de la división es"+str(op1/op2))
    except ZeroDivisionError:
    	print("No se puede dividir entre 0")
    except ValueError:
        print("Los datos ingresados son erróneos")
        ##lo que se incluya dentro de finally siempre se eecutará
    finally:
    	print("Cálculo finalizado")
divide()