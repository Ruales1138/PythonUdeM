# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 17:06:18 2024

@author: b12s208
"""

import random

A = [0] * 20

for i in range(20):
    A[i] = random.randint(1, 30)
print('Vector creado:', A)

cmax = 0

for i in range(20):
    dato = A[i]
    c = 0
    for j in range(20):
        if dato == A[j]:
            c = c+1
    if c > cmax:
        cmax = c
        moda = dato
if cmax == 1:
    print('No hay nada')
else: 
    print(f'La moda del vector es {moda} y esta {cmax} veces')