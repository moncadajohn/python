class Empleado:
	"""docstring for Empleado"""
	def __init__(self, nombre, cargo, salario):
		
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario

	def __str__(self):
		return "{} que trabaxa  como {} tiene un salario de {}$".format(self.nombre, self.cargo, self.salario)

listaEmpleados=[

Empleado("Xuan", "Director", 75000),
Empleado("Ana", "Presidenta", 85000),
Empleado("Antonio", "Administrativo", 25000),
Empleado("Sara", "Investigación", 27000),
Empleado("Mario", "Botones", 21000),

]

salarios_altos=filter(lambda empleado:empleado.salario>50000, listaEmpleados)
for empleado_salario in salarios_altos:
	print(empleado_salario)
		