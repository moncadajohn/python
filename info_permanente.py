import pickle

class Persona():
    def __init__(self,nombre, genero, edad):
	    self.nombre=nombre
	    self.genero=genero
	    self.edad=edad
	    print("se ha creado una persona nueva con el nombre de ",(self.nombre.upper()))
#convertir en cadena de texto la información de un obxeto
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)


class listaPersonas():
	personas=[]

	def __init__(self):
		listaDePersonas=open("ficheroExterno","ab+")
		listaDePersonas.seek(0)

		try:
			self.personas=pickle.load(listaDePersonas)
			print("Se cargaron {} personas en el fichero externo".format(len(self.personas)))
		except:
			print("El archivo está vacío")
		finally:
			listaDePersonas.close()
			del(listaDePersonas)

	def agregaPersonas(self,p):
	    self.personas.append(p)
	    self.guardarPersonasEnFicheroExterno()

	def mostrarPersonas(self):
		for p in self.personas:
		    print(p)

	def guardarPersonasEnFicheroExterno(self):
		listaDePersonas=open("ficheroExterno","wb")
		pickle.dump(self.personas,listaDePersonas)
		listaDePersonas.close()
		del (listaDePersonas)

	def mostrarInfoFicheroExterno(self):
		print("La información del fichero externo es la siguiente: ")
		for p in self.personas:
			print(p)

miLista=listaPersonas()
persona=Persona("Radamel","Masculino",34)
miLista.agregaPersonas(persona)
miLista.mostrarInfoFicheroExterno()