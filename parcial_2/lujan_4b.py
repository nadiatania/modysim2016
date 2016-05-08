from random import random
import math


def g(s, t):
    e = math.e**(-((1.0/t-1.0)+(s+1.0))**2)
    return e*(1.0/t**2)*(1.0/t-1.0)


def experimento(n):
    result = 0.0
    for i in range(n):
        # genero la variable aleatoria u
        u = random()
        # genero la variable aletroia v
        v = random()
        result += g(u, v)
    return float(result/n)

print experimento(100)
print experimento(1000)
print experimento(10000)
print experimento(100000)
