# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:26:52 2024

@author: b12s208
"""
suma = 0
c = 0
prom = 0

for i in range(10):
    numero = int(input('Digita un entero: '))
    print(numero)
    if numero >= 100 and numero <= 200:
        suma = suma + numero
        c = c + 1
if c != 0:
    prom = suma/c

print('El pronedio es', prom)