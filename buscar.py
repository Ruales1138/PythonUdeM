# -*- coding: utf-8 -*-
"""
Created on Fri May  3 17:13:04 2024

@author: b12s208
"""

print('Busqueda Secuencial')

import random

def crearM(n, m):
    A = []
    for i in range(n):
        A.append([0]*m)
    for i in range(n):
        for j in range(m):
            A[i][j] = random.randint(2, 200)
    return A

def buscar(db, M, f, c):
    mens = ''
    for i in range(f):
        for j in range(c):
            if M[i][j] == db:
                mens = 'Detenido'
    return mens

f = int(input('Digita numero de filas\n'))
c = int(input('Digita numero de columnas\n'))
M = crearM(f, c)

print(M)

db = int(input('Digita dato a buscar\n'))
mens = buscar(db, M, f, c)

if mens == '':
    print('No debe nada')
else:
    print(mens)