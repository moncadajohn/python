class Areas:
	
    def areaCuadrado(lado):
	    """función que calcula el área de un cuadrado"""

	    return "El área del cuadrado es: "+str(lado*lado)

	
    def areaTriangulo(base, altura):
	    """función que calcula el área de un Triángulo"""
	    return "El área del triángulo es: "+str((base*altura)/2)



#print(areaCuadrado.__doc__)

#help(areaTriangulo) ayuda de forma individual
help(Areas)