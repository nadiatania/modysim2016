from random import random

def ejerc3_a(n):
	result = 0
	for i in range(n):
		u=random()
		result += (1.0-u**2)**(1.5)
	return result/float(n)

print "Ejercicio 3 a)"
print ejerc3_a(100)
print ejerc3_a(1000)
print ejerc3_a(10000)
print ejerc3_a(100000)
print ejerc3_a(1000000)

def g_b(x):
	return x*((1+x**2)**(-2))
def ejerc3_b(n):
	result = 0
	for i in range(n):
		u = random()
		g=g_b((1.0/u)-1.0)
		denominador = u**2
		result += g/denominador

	return result/float(n)

print "Ejercicio 3 b)"
print ejerc3_b(100)
print ejerc3_b(1000)
print ejerc3_b(10000)
print ejerc3_b(100000)
print ejerc3_b(1000000)

import math
def g_c(x):
	return math.e**(-(x**2))

def ejerc3_c(n):
	result = 0
	for i in range(n):
		u = random()
		g=g_c(1.0/u-1.0)
		result += g/u**2

	return result/float(n)

print "Ejercicio 3 c)"
print ejerc3_c(100)
print ejerc3_c(1000)
print ejerc3_c(10000)
print ejerc3_c(100000)
print ejerc3_c(1000000)


import math
def g_d(x,y):
	return math.e**((x+y)**2)

def ejerc3_d(n):
	result = 0
	for i in range(n):
		u = random()
		v = random()
		result += g_d(u,v)

	return result/float(n)

print "Ejercicio 3 d)"
print ejerc3_d(100)
print ejerc3_d(1000)
print ejerc3_d(10000)
print ejerc3_d(100000)
print ejerc3_d(1000000)