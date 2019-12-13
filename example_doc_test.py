def compruebaMail(mailUsuario):
	"""
	La función compruebaMail evalúa un mail
	recibido en busca de la @ si tiena una @
	es correcto, si tiene más de una @ es incorrecto,
	si  la @ está al final es incorrecto

	>>> compruebaMail('xuan@cursos.es')
	True

	"""
	arroba=mailUsuario.count('@')
	if(arroba!=0 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0):
		return False
	else:
		return True

import doctest
doctest.testmod()