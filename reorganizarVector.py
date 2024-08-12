# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 16:29:13 2024

@author: b12s208e20
"""

print('programa que reordena un vector')

import random
A=[0]*20
P=[0]*20
I=[0]*20

for i in range(20):
    A[i]=random.randint(1,30)
print('vector creado ',A)

#aquí reordeno el vector colocando pares y luegp impares
j=0
#el primer for es para colocar los pares
for i in range(20):
    if A[i]%2==0:
        P[j]=A[i]
        j+=1
j=0        
for i in range(20):
     if A[i]%2!=0:
         I[j]=A[i]
         j+=1
print(f'el vector de pares es: {P}')
print(f'el vector de impares es: {I}') 