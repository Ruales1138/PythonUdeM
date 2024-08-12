# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:04:31 2024

@author: b12s208
"""

"""
for i in range(5, 51):
    if i % 5 == 0:
        print(i)
"""

iteracion = 0

for i in range(5, 51, 5):
    print(i)
    iteracion += 1
    
print(f'El proceso se repite {iteracion} veces')