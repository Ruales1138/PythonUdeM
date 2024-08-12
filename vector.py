# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:00:00 2024

@author: b12s208
"""
Vector = ['*']*4
print(Vector)

for i in range(4):
    dato = input('Digita una palabra: ')
    print(i, dato)
    Vector[i] = dato
print('El vector creado es', Vector)
