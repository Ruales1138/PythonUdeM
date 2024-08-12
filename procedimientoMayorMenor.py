# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:37:30 2024

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

def mayMen(A):
    mayor = A[0][0]; menor = A[0][0]
    for i in range(f):
        for j in range(c):
            if A[i][j] > mayor:
                mayor = A[i][j]
                iM = i
                jM = j
            if A[i][j] < menor:
                menor = A[i][j]
                im = i
                jm = j
    return mayor, menor, iM, jM, im, jm

print('Digita numero de filas y columnas para la matriz\n')
f = int(input(''))
c = int(input(''))
A = crearMat(f, c) # Aqui llamo la funcion para imprimir la matriz

for i in A:
    print(i)
    
# Aqui llamamos el procedimiento mayMen

may, men, iM, jM, im, jm = mayMen(A)
print(f'El elemnto mayor es {may} y el menor es {men}')
print(f'El mayor esta en posicion ({iM + 1}, {jM + 1})')
print(f'El menor esta en posicion ({im + 1}, {jm + 1})')