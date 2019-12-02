"""
qué es serialización:
guardar en un archivo externo  una colección, un diccionario
o incluso un obxeto con la particularidad de guardarlo en un archivo
externo codificado en código binario

BIBLIOTECAS NECESARIAS
Pickle:
Método dump():volcado de datos al fichero binario externo
Método load():carga de los datos del fichero binario externo
"""

import pickle

lista_nombres=["pedro","ana","maria","isabel"]

fichero_binario=open("lista_nombres","wb")#esto significa que será de escritura binaria

pickle.dump(lista_nombres,fichero_binario)
fichero_binario.close()

del (fichero_binario)#borrar de memoria