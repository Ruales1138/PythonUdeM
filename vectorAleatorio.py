# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:45:07 2024

@author: b12s208
"""

import random as rd

n = int(input('Digita el rango para tu vector: '))
R = [0]*n

for i in range(n):
    #R[i] = rd.random()*200 # Para generar numeros entre 0 y 200
    R[i] = rd.randint(1, 200) # Para numero entre 1 y 200
print('El vector creado fue ', R)

# Aqui encontramos el numero mayor del vector

mayor = R[0]

for i in range(n):
    if R[i] > mayor:
        mayor = R[i]
print('El elemento mayor es ', mayor)

# Aqui encontramos el numero menor del vector

menor = R[0]

for i in range(n):
    if R[i] < menor:
        menor = R[i]
print('El elemento menor es ', menor)

# Calcular el promedio

suma = 0

for i in range(n):
    suma = suma + R[i]
promedio = suma/n
print('Promedio: ', promedio)