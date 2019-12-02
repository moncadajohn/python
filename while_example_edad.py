edad = int(input("introduce tu edad : "))

while edad<0:
      print("Edad negativa, vuelve a digitarla")
      edad = int(input("introduce tu edad : "))

if edad>100:
    print("Edad de",edad,"no es muy acorde")
else:
    print("la edad es correcta")
    print("tu edad es ",edad)

        