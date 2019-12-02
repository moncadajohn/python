class Coche():
	largoChasis = 250
	anchoChasis = 120
	ruedas = 4
	enmarcha = False

	##creación de un método
	##self hace referencia a la instancia perteneciente a la clase, es casi igual que this

	def arrancar(self):
		self.enmarcha=True

	def estado(self):
	    if(self.enmarcha):
	    	return "El coche está en marcha"
	    else:
	    	print("El coche está detenido")

print("----------creación de primera instancia/obeto-------")
#creación de obeto o instancia
miCoche = Coche()#esto se llama instanciar una clase/instanciación de clase/eemplarizar una clase

print("El largo del coche es ",miCoche.largoChasis)
miCoche.arrancar()
print(miCoche.estado())		


print("----------creación de segunda instancia/obeto-------")

miCoche2 = Coche()
print("El largo del coche es ",miCoche2.largoChasis)
miCoche2.arrancar()
print(miCoche2.estado())		
