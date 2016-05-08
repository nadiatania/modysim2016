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


def experimento(n):
    k = 1000000
    exitos = 0
    for _ in range(k):
        num = calcular_n()
        if num == n:
            exitos += 1
    print "P(N = " + str(n) + ") = " + str(exitos/float(k))

experimento(0)
experimento(1)
experimento(2)
experimento(3)
experimento(4)
experimento(5)
experimento(6)
