class Coche():
  """docstring for Coche"""
  def desplazamiento(self):
    print("Me desplazo utilizando cuatro ruedas")

class Moto():
  def desplazamiento(self):
    print("Me desplazo utilizando dos ruedas")


class Camion():
  def desplazamiento(self):
    print("Me desplazo utilizando seis ruedas")

##Utilización del polimorfismo

def desplazamientoVehiculo(vehiculo):
  vehiculo.desplazamiento()

miVehiculo=Moto()
desplazamientoVehiculo(miVehiculo)

"""
miVehiculo=Moto()
miVehiculo.desplazamiento()


miVehiculo1=Coche()
miVehiculo1.desplazamiento()


miVehiculo2=Camion()
miVehiculo2.desplazamiento()
"""

##desplazamiento es un método o comportamiento



    