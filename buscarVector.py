# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:18:37 2024

@author: b12s208
"""
import random as rd

def binaria(V, k):
    bajo = 0
    alto = n
    pcentral = (bajo + alto) // 2
    while bajo <= alto and k != V[pcentral]:
        if k < V[pcentral]:
            alto = pcentral - 1
        else:
            bajo = pcentral + 1
        pcentral = (bajo + alto) // 2
    if k == V[pcentral]:
        mensaje = 'Dato encontrado'
    else:
        mensaje = 'Dato no encontrado'
    return mensaje

def crearV(rango):
    A = [0] * rango
    for i in range(rango):
        A[i] = rd.randint(0, 200)
    return A

def Burbuja(V, n):
    for i in range(1, n):
        for j in range(0, n-i):
            if V[j] > V[j+1]:
                aux = V[j]
                V[j] = V[j + 1]
                V[j+1] = aux
    return V

n = int(input('Dime el rango para imprimir el vector\n'))

V = crearV(n)
print('Vector generado: ', V)

V_sort = Burbuja(V, n)
print('El vector ya ordenado es: ', V_sort)

db = int(input('Dime el dato que quieres encontrar\n'))
mensaje = binaria(V_sort, db)
print(mensaje)