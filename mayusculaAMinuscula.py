# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 17:01:55 2024

@author: b12s208
"""

def convertir(oracion):
    oracionConvertida = oracion.lower()
    return oracionConvertida

# Principal

mensaje = input('Ingrese la palabra\n')
OC = convertir(mensaje)
print(OC)