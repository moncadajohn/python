class Vehiculos():
   #Creación del constructor
  def __init__(self, marca, modelo):
      self.marca=marca
      self.modelo=modelo
      self.enmarcha=False
      self.acelera=False
      self.frena=False

  def arrancar(self):
      self.enmarcha=True

  def acelerar(self):
      self.acelera=True

  def frenar(self):
      self.frena=True

  def estado(self):
      print("Marca :",self.marca, 
            "\nModelo: ",self.modelo,
            "\nEn Marcha: ", self.enmarcha,
            "\nAcelerando: ",self.acelera,
            "\nFrenando: ", self.frena)

class Furgoneta(Vehiculos):
  def carga(self,cargar):
    self.cargado=cargar
    if (self.cargado):
      return "La Furgoneta está cargada"
    else:
      return "La Furgoneta no está cargada"


#Creación de la herencia múltiple, porque hereda 5 métodos más su método propio

class Moto(Vehiculos):
  hcaballito=""
  def caballito(self):
    self.hcaballito="Voy haciendo caballito"

  def estado(self):
      print("Marca :",self.marca, 
            "\nModelo: ",self.modelo,
            "\nEn Marcha: ", self.enmarcha,
            "\nAcelerando: ",self.acelera,
            "\nFrenando: ", self.frena,
            "\n",self.hcaballito)

class VElectricos():
  def __init__(self):
    self.autonomia=100

  def cargarEnergia(self):
    self.cargando=True

##Lo que ocurrió fue que el método estado copiado en la clase moto sobre escribe el de la clase  padre.(sobre escritura o sobre carga de métodos)

miMoto=Moto("Honda","CBR")
miMoto.caballito()
print(miMoto.estado())
print("*******************************")

miFurgoneta=Furgoneta("Renault","Duster")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))
print("*******************************")

##herencia múltiple
class BicicletaElectrica(VElectricos,Vehiculos): #prima el orden en que se llaman las clases
  pass

miBici=BicicletaElectrica()
  