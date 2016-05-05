from random import random
import math

def g(x):
	return math.e**(-x)

def f(y):
	return math.e**(-(1.0/y-1.0))*(1.0/y**2)

def experimento(n):
	#Separo los resultados de las 2 integrales
	result_1 = 0.0
	result_2 = 0.0
	for i in range(n):
		#genero variable aleatoria en 0,1
		u = random()
		result_1 += g(u)
		result_2 += f(u)

	result_1 = float(result_1/n) #Reemplazo el resultado con el promedio
	result_2 = float(result_2/n) 
	return result_2-result_1 #la suma de las 2 integrales, result_1 es negativa
	

print experimento(100)
print experimento(1000)
print experimento(10000)
print experimento(100000)

