from random import random, normalvariate
import math


def experimento():
    x = normalvariate(0, 1)
    m = x
    var = 0.0
    for j in range(2, 30):
        x = normalvariate(0, 1)
        a = m
        m = m + (x - m)/float(j)
        var = (1.0 - 1.0/(j-1))*var + j*(m-a)**2
    j = 30
    while (math.sqrt(var/float(j)) > 0.1):
        j = j + 1
        x = normalvariate(0, 1)
        a = m
        m = m + (x - m)/float(j)
        var = (1.0 - 1.0/(j - 1)) * var + j * (m - a)**2

    return m, var, j

print experimento()
count = 0
for i in range(1000):
    m, var, j = experimento()
    count += j

print count / float(1000)
