# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 16:04:35 2024

@author: b12s208
"""
# Aqui reservamos espacio en memoria para la matriz

C = []
n = int(input('Ingresa el rango para tu matriz\n'))

for i in range(n):
    C.append([0] * n)
    
for i in C:
    print(i)
    
# Aqui generamos la matriz con datos aleatorios

import random

for i in range(n):
    for j in range(n):
       # C[i][j] = random.randint(1, 200)
       C[i][j] = round(random.random()*100,2)

for i in C:
    print(i)
    
# Aqui sumamos los elementos de las diagonales

sp = 0; ss = 0

for i in range(n):
    for j in range(n):
        if i == j:
            sp = sp + C[i][j]
        if i + j == n-1:
            ss += C[i][j]
            
print(f'La suma de la diagonal principal es: {sp}')
print(f'La suma de la diagonal secundaria es: {ss}')

