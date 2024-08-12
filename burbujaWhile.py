# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:56:58 2024

@author: b12s208
"""

import random as rd

def crearVector(n):
    A=[0]*n
    for i in range(n):
        A[i]=rd.randint(1,200)
    return A



def burbujaAsc(B):
    i = 0
    while i < rango:
        j = 0
        while j < i:
            if B[j]>B[j+1]:
                aux=B[j]
                B[j]=B[j+1]
                B[j+1]=aux
            j = j+1
        i = i+1
    return B

def burbujaDesc(B):
    i = 0
    while i < rango:
        j = 0
        while j < i:
            if B[j]<B[j+1]:
                aux=B[j]
                B[j]=B[j+1]
                B[j+1]=aux
            j = j+1
        i = i+1
    return B



#ppal
rango = int(input('Digita el rango del vector que quieres generar \n'))
B = crearVector(rango)
print('El vector generado es:  ', B)

sortB=burbujaAsc(B)

print('El vector ordenado es: ',sortB)

sortBdesc=burbujaDesc(B)

print('El vector ordenado de manera descente es: ',sortBdesc)