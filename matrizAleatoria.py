# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 16:37:45 2024

@author: b12s208
"""

print('Matriz aleatoria')

import random as rd

filas = int(input('Numero de filas\n'))
columnas = int(input('Numero de columnas\n'))

A=[]

for i in range(filas):
    A.append([0] * columnas)

for i in range(filas):
    for j in range(columnas):
        A[i][j] = round(rd.random()*100,2)
        
for i in A:
    print(i)
    