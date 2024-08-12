# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:28:20 2024

@author: b12s208
"""

def Cuadrado(l):
    p = 4*l
    a = l**2
    return p,a
    
# Principal

lado = float(input('Digita la medida del lado\n'))
perimetro, area = Cuadrado(lado)

print(f'Perimetro {perimetro} y area {area}')