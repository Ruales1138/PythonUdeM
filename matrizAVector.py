# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 17:14:05 2024

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
    
print('----------------------------------------------------------------------')
    
# Aqui reservo espacios para el vector

V = [0] * (n*n)

# Aqui voy llevando cada elemento de la matriz al vector

K = 0

for i in range(n):
    for j in range(n):
        V[K] = C[i][j]
        K = K+1
        
print('El vector con elementos de la matris es:', V)

