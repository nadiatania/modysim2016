import random

def barajada():
	baraja = []
	k = 99
		
	for i in range(k+1):
		baraja.append(i+1)
	
	while (k > 0):
		u = random.random()
		i = int(k * u) +1
		# Aca swapeamos las posiciones de las cartas
		aux = baraja[i]
		baraja[i] = baraja[k]
		baraja[k] = aux
		k -=1
	return baraja

def experimento():
	
	exitos = 0
	baraja = barajada()
		
	for i in range(100):
		if baraja[i] == i+1:
			exitos += 1
	return exitos

def calcular_esperanza_varianza(n):

	suma1 = 0.0
	suma2 = 0.0
	
	for _ in range(n):
		x = experimento()
		suma1 += x
		suma2 += x**2

	esperanza = suma1 / float(n)
	varianza = suma2 / float(n) - esperanza**2
	print esperanza, varianza
	
calcular_esperanza_varianza(10)
calcular_esperanza_varianza(100)
calcular_esperanza_varianza(1000)
calcular_esperanza_varianza(10000)