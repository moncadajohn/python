def areaTriangulo(base, altura):

	"""
	calcula el área de un triángulo dado

	>>> areaTriangulo(3,6)
	8.0

	"""
	
	return (base*altura)/2

#print(areaTriangulo(2,4))
import doctest
doctest.testmod()