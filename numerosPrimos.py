# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 17:02:07 2024

@author: b12s208
"""

for numero in range(100):
    cd = 0

    for i in range(1, numero + 1):
        if numero % i == 0:
            cd += 1      
    if cd == 2:
        print(numero)

