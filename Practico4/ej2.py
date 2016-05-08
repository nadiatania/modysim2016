from math import e
from random import random

def experiemento(n):
	s = 0
	N=10000
	for _ in range(n):
		u = random()
		x = int(N*u)+1 	
		s += e**(x/float(N))

	return s*n

print experiemento(100)