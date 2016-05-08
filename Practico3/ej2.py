from random import random


def ejer2(n):
    exitos = 0
    x = 0
    for i in range(n):
        u = random()
        if (u < 0.5):
            x = random() + random()
        else:
            x = random() + random() + random()
    if(x >= 1.0):
        exitos += 1.0

    return exitos / float(n)

print ejer2(100)
print ejer2(1000)
print ejer2(10000)
print ejer2(100000)
