from random import random
from math import log
NRO_OPER = 1
TF = 1
TR = 1.0/8.0
N = 5
S = 2
# Generar los tiempos de falla con una variable aleatoria exponencial con
# parametro lambda = TF


def generar_va_exponencial(lamda):
    u = random()
    x = - 1/float(lamda)*log(u)

    return x


def experimento(n, NRO_OPER, TF, TR, N, S):
    t = 0
    r = 0
    t_ = float("inf")
# registro de los instantes en que las maquinas fallan
    t_maq_fallan = []
# registro en que la maquina concluyen su reparacion
    t_maq_rep = []
    for _ in range(n):
        t_maq_fallan.append(generar_va_exponencial(1.0/TF))

    t_maq_fallan.sort()
    i = 0
    while True:
        if t_maq_fallan[i] < t_:
            t = t_maq_fallan[i]
            r += 1
            if r == S + 1:
                # No hay repuesto
                return t
            elif r < S + 1:
                i = i + 1
                t_maq_fallan.append(t + generar_va_exponencial(1/TF))
                t_maq_fallan.sort()
            elif r == NRO_OPER:
                y = generar_va_exponencial(1/TR)
                t_ = t + y
        else:
            t = t_
            r = r - 1
            if r > 0:
                y = generar_va_exponencial(1/TR)
                t_ = t + y
            elif r == 0:
                t_ = float('inf')
                break


print experimento(100, NRO_OPER, TF, TR, N, S)
