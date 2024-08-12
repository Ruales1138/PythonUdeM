# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 17:08:58 2024

@author: b12s208
"""
import random

def crearMatriz(f,c):
    M = []
    for i in range(f):
        M.append([0]*c)
    for i in range(f):
        for j in range(c):
            M[i][j] = random.randint(0,300)
    return M

def sumaMatriz(M, filas, columnas):
    suma = 0
    for i in range(filas):
        for j in range(columnas):
            suma += M[i][j]
    return suma

# Principal

filas = int(input('Digita el numero de filas\n'))
columnas = int(input('Digita el numero de columnas\n'))

# Aqui invoco la funcion para crear la matriz

matriz = crearMatriz(filas, columnas)

for i in matriz:
    print(i)
    
# Aqui invoco la funcion para sumar los elementos de la matriz

s = sumaMatriz(matriz, filas, columnas)

print(f'La suma de los elementos es: {s}')