from random import random
from math import log, sqrt

#  Generar los tiempos de falla con una variable aleatoria exponencial con
#  parametro lambda = TF


def generar_va_exponencial(lamda):
    u = random()
    x = - 1/float(lamda)*log(u)

    return x


def experimento(N, S, TF, TR, NRO_OPER):
    t = 0  # variable de tiempo
    r = 0  # cantidad de maquinas rotas
    t_maq_fallan = []  # registro de los instantes en que las maquinas fallan
    t_maq_rep = []  # registro en que la maquina concluyen su reparacion

    # Genero tiempos de falla con una va exponencial de media 1/TF
    for _ in range(N):
        t_maq_fallan.append(generar_va_exponencial(1.0 / TF))
    # el registro de maquinas en reparacion es infinito puesto q no hay maq
    # en reparacion
    for _ in range(NRO_OPER):
        t_maq_rep.append(float("inf"))
    # Ordeno las maquinas que fallan
    t_maq_fallan.sort()
    while True:
        if t_maq_fallan[0] < min(t_maq_rep):
            t = t_maq_fallan[0]
            r += 1  # puesto que ha fallado una maquina
            t_maq_fallan.pop(0) #quito el primer elemento de la lista
            if r == S + 1:
                # No hay repuesto
                return t  # Devuelvo el tiempo de fallo
            if r < S + 1:
                # Genero una va exponencial
                X = generar_va_exponencial(1.0 / TF)  # Representa el tiempo de
                # trabajo del repuesto a funcionar
                t_maq_fallan.append(t + X)
                t_maq_fallan.sort()  # Ordeno los valores nuevos
            if r <= NRO_OPER:  # Tengo operarios disponibles para repararcion
                # Busco un operario disponible
                for i in range(NRO_OPER):
                    if t_maq_rep[i] == float("inf"):
                        # Genero una va exponencial  del tiempo de reparacion
                        Y = generar_va_exponencial(1.0 / TR)
                        t_maq_rep[i] = t + Y
        else:  # No hay fallo antes de que una maquina sea reparada
            for i in range(NRO_OPER):
                if t_maq_rep[i] == min(t_maq_rep):
                    t = min(t_maq_rep)
                    r = r - 1
                    if r > NRO_OPER - 1:  # todavia hay maquinas esperando ser
                        # reparadas
                        Y = generar_va_exponencial(1.0 / TR)
                        t_maq_rep[i] = t + Y
                    else:
                        t_maq_rep[i] = float('inf')
                    break

def calcular_esperanza_desviacion(n):
    sum_0 = 0.0
    sum_1 = 0.0
    TF = 1
    TR = 1.0/8.0
    N = 5
    S = 2
    for _ in range(n):
        x = experimento(N, S, TF, TR, 2)
        sum_0 += x
        sum_1 += x**2
    esperanza = sum_0 / float(n)
    varianza = sum_1 / float(n) - esperanza**2
    desv_estandar = sqrt(varianza)
    print "Tiempo de fallo promedio: " + str(esperanza)
    print "Desviacion estandar: " + str(desv_estandar)
    return esperanza, desv_estandar

calcular_esperanza_desviacion(10)