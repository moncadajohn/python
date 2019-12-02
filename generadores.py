"""forma normal
def generapares(limite):
	num=1
	miLsta=[]
	while num<limite:
		miLsta.append(num*2)
		num=num+1
	return miLsta
print(generapares(10))
"""
##utilizando yield

def generapares(limite):
	num=1
	while num<limite:
		yield num*2
		num=num+1
devuelvepares=generapares(10)
#for i in devuelvepares:
	#print(i)  ##utilizaremos ahora next

print(next(devuelvepares))
print("Aquí podría ir más codigo")

print(next(devuelvepares))
print("Aquí podría ir más codigo")

print(next(devuelvepares))
print("Aquí podría ir más codigo")

