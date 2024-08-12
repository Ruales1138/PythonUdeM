# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 16:04:25 2024

@author: b12s208
"""

print('Matriz de cadenas')

S=[]

for i in range(3):
    S.append(['*'] * 2)
    
#print(S)

for i in S:
    print(i)
    
# Aqui ingrsamos los elementos de la matriz

for i in range(3):
    for j in range(2):
        nombre = input('Digita nombre\n')
        S[i][j] = nombre
        
# Aqui mostramos la matriz creada

for i in S:
    print(i)
        