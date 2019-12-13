print("calcular sueldo y gastos")

ingreso = int(input("Ingrese el sueldo devengado: $"))

def segSocial(calculo):
    calculo = ingreso*4/100
    return calculo*2

#segSocial(ingreso)

arriendo=500000
pasaxes=100000
internet_tv=130000
almuerzos=100000
falabella=120000
celulares=130000
agua=80000
movistar=75000
prestamo=412000
mercado=100000


pagos_mensuales = arriendo+pasaxes+internet_tv+almuerzos+falabella+celulares+agua+movistar+prestamo+mercado

pagos=pagos_mensuales+segSocial(ingreso)

total=ingreso-pagos

print("SUELDO............................:$",ingreso)
print("SEGURIDAD SOCIAL SALUD/PENSIÓN 4%.:$",segSocial(ingreso))
print("RESPONSABILIDADES MENSUALES.......:$",pagos_mensuales)
print("TOTAL PAGOS.......................:$",pagos)
print("VALOR DISPONIBLE..................:$",total)

