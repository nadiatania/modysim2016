import random
import math

def calcular_n():
    n = 0
    m = 1
    while m >= math.exp(-3):
        m *= random.random()
        n += 1
    n -= 1
    return n

def experimento(k):
    res = 0
    for _ in range(k):
        res += calcular_n()
    print "Esperanza (n = " + str(k) + "):" + str(res/float(k))

experimento(100)
experimento(1000)
experimento(10000)
experimento(100000)
experimento(1000000)