# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 16:40:37 2024

@author: b12s208
"""

print('Programa para buscar un dato en vector')
print('----------------------------------------------------------------------')

n = int(input('Digite cantidad de datos para el vector\n'))
S = ['*'] * n

for i in range(n):
    elemento = input('Digita una palabra\n')
    S[i] = elemento
print('El vector generado es:', S)


print('----------------------------------------------------------------------')

c = 0
B = False
db = input('Ingreasa dato a buscar\n')

for i in range(n):
    if db == S[i]:
        c += 1
        B = True
        
if B == False:
    print('Dato no encontrado')
else:
    print(f'Dato buscado esta {c} veces')