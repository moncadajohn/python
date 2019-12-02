class Coche():

#CREACIÓN DEL CONSTRUCTOR
##CONSTRUCTOR
#Método especial que le da estado inicial a los obetos
#forma de especificar claramente cuál va a ser el estado inicial de los obetos qu pertenecen a una clase



    def __init__(self):

    	#Encapsular : proteger las variables de posibles cambios
    	#se encapsula anteponiendo dos líneas baxas : __variable

       self.__largoChasis = 250
       self.__anchoChasis = 120
       self.__ruedas = 4
       self.__enmarcha = False

	##creación de un método
	##self hace referencia a la instancia perteneciente a la clase, es casi igual que this

    def arrancar(self, arrancamos):
        self.__enmarcha=arrancamos
        if(self.__enmarcha):
          chequeo=self.__chequeo_interno()

        if(self.__enmarcha and chequeo):
            return "El coche está en marcha"
        elif(self.__enmarcha and chequeo=="False"):
            return "Algo ha ido mal en el chequeo. No podemos arrancar"
        else:
            print("El coche está detenido")

    def estado(self):
	    print("El coche tiene",self.__ruedas,"ruedas, un ancho de ",self.__anchoChasis,
	    	"y un largo de", self.__largoChasis)

    def __chequeo_interno(self):
      print("Realizando chequeo interno del vehículo")
      self.gasolina="ok"
      self.aceite="ok"
      self.puertas="cerradas"

      if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
        return True
      else:
        return False

print("----------creación de primera instancia/obxeto-------")
#creación de obeto o instancia
miCoche = Coche()#esto se llama instanciar una clase/instanciación de clase/eemplarizar una clase
print(miCoche.arrancar(True))
miCoche.estado()
	


print("----------creación de segunda instancia/obeto-------")

miCoche2 = Coche()
miCoche2.__ruedas=3
miCoche2.arrancar(False)
miCoche2.estado()

