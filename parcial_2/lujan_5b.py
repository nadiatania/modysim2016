from random import random

def experimento(n):
	exitos=0.0
	for i in range(n):
		u=random()
		v=random()
		#si el primero es menos a 1/2 y el segundo es mayor que el primero
		if(u<0.5 and v>u):
			exitos += 1.0
		#si el primero es mayor a 1/2 y el segundo es menos al primero
		elif(u>0.5 and v<u):
			exitos += 1.0

	return float(exitos/n)
		
print experimento(100)
print experimento(1000)
print experimento(10000)
print experimento(100000)
