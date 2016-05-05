from random import random, normalvariate
import math

def generar_x():
    u = random()
    x = math.exp(u**2)
    return x
def experimento():
    x = generar_x()
    m = x
    var = 0.0
    for j in range(2, 100):
        x = generar_x()
        a = m
        m = m + (x - m)/float(j)
        var = (1.0 - 1.0/(j-1))*var + j*(m-a)**2
    j = 100
    while (math.sqrt(var/float(j)) > 0.01):
        j = j + 1
        x = generar_x()
        a = m
        m = m + (x - m)/float(j)
        var = (1.0 - 1.0/(j - 1)) * var + j * (m - a)**2

    return m, var, j

print experimento()
