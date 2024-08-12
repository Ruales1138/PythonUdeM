# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 16:05:17 2024

@author: b12s208
"""

def rectangulo(b,h):
    p = 2*b+2*h
    return p

# Principal

base = float(input('Digita la medida de la base\n'))
altura = float(input('Digita la medida de la altura\n'))

perimetro = rectangulo(base, altura)

print(f'El perimetro es: {perimetro}')