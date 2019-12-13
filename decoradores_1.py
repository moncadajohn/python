#DECORADORES
"""SON FUNCIONES QUE A SU VEZ AÑADEN FUNCIONALIDADES A OTRAS FUNCIONES.
LES AÑADEN FUNCIONALIDADES

UN DECORADOR DEVUELVE OTRA FUNCIÓN

def función_decorador(funcion):  ##función A
	def función_interna():       ##función B
		#código de la función interna
	return función interna       ##función C
"""

def funcion_decoradora(funcion_parametro):
	def funcion_interior(*args, **kwargs):
		#Acciones adicionales que decoran
		print("Vamos a realizar un cálculo")

		funcion_parametro(*args, **kwargs)#con este término admite clave - valor **kwargs

		#Acciones adicionales que decoran

		print("Hemos terminado el cálculo")

	return funcion_interior



@funcion_decoradora
def suma(num1, num2):
	print(num1+num2)

@funcion_decoradora
def resta(num1, num2):
	print(num1-num2)

@funcion_decoradora
def potencia1(base, exponente):
	print(pow(base, exponente))




suma(7,5)
resta(12,10)
potencia1(base=2,exponente=8)