from random import random
from math import log, sqrt
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
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
                        break
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

def calcular_esperanza_desviacion(n, S, NRO_OPER):
    sum_0 = 0.0
    sum_1 = 0.0
    TF = 1
    TR = 1.0/8.0
    N = 5
    for _ in range(n):
        x = experimento(N, S, TF, TR, NRO_OPER)
        sum_0 += x
        sum_1 += x**2
    esperanza = sum_0 / float(n)
    varianza = sum_1 / float(n) - esperanza**2
    desv_estandar = sqrt(varianza)
    print "Tiempo de fallo promedio: " + str(esperanza)
    print "Desviacion estandar: " + str(desv_estandar)
    return esperanza, desv_estandar

print "\nCaso 1: 2 maquinas de repuesto y 1 operario"
calcular_esperanza_desviacion(10000, 2, 1)
print "\nCaso 2: 2 maquinas de repuesto y 2 operarios"
calcular_esperanza_desviacion(10000, 2, 2)
print "\nCaso 3: 3 maquinas de repuesto y 1 operario"
calcular_esperanza_desviacion(10000, 3, 1)


########################################################################
tiempos_de_fallo_c1 = []
for _ in range(10000):
    tiempos_de_fallo_c1.append(experimento(5, 2, 1, 1.0/8.0, 1))

plt.title("Caso 1: 5 Maquinas funcionando, 2 de repuesto y 1 operario")
plt.xlabel("Tiempo de falla en Meses")
plt.ylabel("Frecuencia Relativa de las simulaciones")
bins = np.linspace(0, 30, 50)
plt.hist(tiempos_de_fallo_c1, 10, normed=True, color='r')
plt.show()


########################################################################
tiempos_de_fallo_c2 = []
for _ in range(10000):
    tiempos_de_fallo_c2.append(experimento(5, 2, 1, 1.0/8.0, 2))
bins = np.linspace(0, 30, 50)
plt.title("Caso 2: 5 Maquinas funcionando, 2 de repuesto y 2 operarios")
plt.xlabel("Tiempo de falla en Meses")
plt.ylabel("Frecuencia Relativa de las simulaciones")
plt.hist(tiempos_de_fallo_c2, 10, normed=True, color='g')
plt.show()

########################################################################
tiempos_de_fallo_c3 = []
for _ in range(10000):
    tiempos_de_fallo_c3.append(experimento(5, 3, 1, 1.0/8.0, 1))

plt.title("Caso 3: 5 Maquinas funcionando, 3 de repuesto y 1 operario")
plt.xlabel("Tiempo de falla en Meses")
plt.ylabel("Frecuencia Relativa de las simulaciones")

plt.hist(tiempos_de_fallo_c3, 10, normed=True, color='y')
plt.show()

##################################################################
#plt.figure(figsize=(9, 8))
plt.title("Comparaciones:\nCaso 2 vs. Caso 3")
plt.xlabel("Tiempo de falla en Meses")
plt.ylabel("Frecuencia Relativa de las simulaciones")
#bins = np.arange(min(bins), max(bins)+1, 1.0) 
bins = np.linspace(0, 10, 40)
plt.hist(tiempos_de_fallo_c2, alpha=0.7, bins=10, normed=True, label='Caso 2', color='b')
plt.hist(tiempos_de_fallo_c3, alpha=0.5, bins=10, normed=True, label='Caso 3', color='r')
#plt.xticks(np.arange(min(bins), max(bins)+1, 1.0))

plt.legend()
plt.show()
