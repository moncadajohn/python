import pickle



class Vehiculo():
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

coche1=Vehiculo("Mazda","CX3")

coche2=Vehiculo("Volkswagen","Golf")

coche3=Vehiculo("Hyundai","i20")

coches=[coche1,coche2,coche3]#colección de obxetos de tipo coche

fichero=open("loscoches","wb")#escritura de bytes

#hacer el volcado de información al fichero que se acaba de crear

pickle.dump(coches,fichero)
fichero.close()

del(fichero)#borrar archivo de la memoria


##ABRIR EL FICHERO NUEVAMENTE

ficheroApertura=open("loscoches","rb")
#creo variable en donde cargaré la información de dicho fichero
misCoches=pickle.load(ficheroApertura)
ficheroApertura.close()

for c in misCoches:
  print(c.estado())




