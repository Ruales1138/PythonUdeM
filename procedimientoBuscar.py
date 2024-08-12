# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:09:29 2024

@author: b12s208
"""

import random as rd

def crearMat(f,c):
    M=[]
    for i in range(f):
        M.append([0]*c)
    for i in range(f):
        for j in range(c):
            M[i][j] = rd.randint(1, 40)
    return M

def buscarDato(A, db):
    mensaje = 'Dato no encontrado'
    for i in range(f):
        for j in range(c):
            if A[i][j] == db:
                mensaje = 'Dato encontrado'
    return mensaje

print('Digita numero de filas y columnas para la matriz\n')
f = int(input(''))
c = int(input(''))
A = crearMat(f, c) # Aqui llamo la funcion para imprimir la matriz

for i in A:
    print(i)
    
# Llamo la funcion para buscar un dato

db = int(input('¿Que numero quieres buscar?: '))
mens = buscarDato(A, db)
print(mens)