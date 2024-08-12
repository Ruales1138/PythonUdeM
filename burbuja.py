# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:10:01 2024

@author: b12s208
"""

print('Programa modular para crear y organizar un vector')
import random
def crearV(n):
    B=[0]*n
    for i in range(n):
        B[i]=random.randint(0,200)
    return B



def burbujaAsc(B,n):
   for i in range(1,n):
       for j in range(0,n-i):
           if B[j]>B[j+1]:
               aux=B[j]
               B[j]=B[j+1]
               B[j+1]=aux
   return B


def burbujaDesc(B,n):
   for i in range(1,n):
       for j in range(0,n-i):
           if B[j]<B[j+1]:
               aux=B[j]
               B[j]=B[j+1]
               B[j+1]=aux
   return B


#ppal
n=int(input('Digita el rango del vector que quieres generar \n'))
B=crearV(n)
print('El vector generado es:  ', B)

sortB=burbujaAsc(B,n)

print('El vector ordenado es: ',sortB)

sortBdesc=burbujaDesc(B, n)

print('El vector ordenado de manera descente es: ',sortBdesc)