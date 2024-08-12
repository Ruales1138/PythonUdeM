# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 16:12:47 2024

@author: b12s208
"""

print('Programa para el control del virus chukunguña')
casosP = 0; casosN = 0; casosF = 0; casosm = 0; casosM = 0; casosA = 0; casosR = 0; casosU = 0
i = 1
while i <= 5:
    # Varibles de entrada
    resultado = input('Ingrese resultado del analisis: "p" para positivo o "n" para negativo: \n')
    edad = int(input('Digita edad del paciente: \n'))
    # Asignacion de rango
    if edad < 18:
        rango = 'menor'
    elif edad >= 18 and edad < 60:
        reango = 'adulto'
    elif edad >= 60:
        rango = 'mayor'
    genero = input('Ingrese genero del paciente: "m" / "f": \n')
    zona = input('Ingrese zona de recidencia: "r" para rural o "u" para urbana: \n')
    # Esto es para calcular los porcentajes positivos y negativos
    if resultado == 'p':
        casosP +=1
    if resultado == 'n':
        casosN +=1
    if genero == 'f' and resultado == 'p' and zona == 'r':
        casosF +=1
    if rango == 'menor':
        casosm +=1
    if rango == 'adulto':
        casosA +=1
    if rango == 'mayor':
        casosM += 1
    # Aqui determinamos las zonas mas afectadas (urbana o rural)
    if zona == 'r':
        casosR +=1
    if zona == 'u':
        casosU +=1
    i +=1

print('---------------------------------------------------------')
# Porcentaje de casos
print('El porcenraje de casos positivos fue', casosP/5*100, '%')
print('El porcenraje de casos negativos fue', casosN/5*100, '%')
print('---------------------------------------------------------')
# Casos especiales
print(f'El numero de pasientes femeninos positivos y de zona rural fueron: {casosF}')
print('---------------------------------------------------------')
# Sector de la poblacion mas afectedo por rango de edad
if casosm > casosA and casosm > casosM:
    print('La poblacion mas afectada fueron los menores de 18 años')
if casosm < casosA and casosm > casosM:
    print('La poblacion mas afectada fueron los menores de 18 años')
if casosM > casosA and casosm < casosM:
    print('La poblacion mas afectada fueron los menores de 18 años')
print('---------------------------------------------------------')
# Aqui se determina donde se dieron mas casos si en el campo o en la ciudad
if casosR > casosU:
    print('Se presentaon mas casos en la zona rural')
if casosR < casosU:
    print('Se presentaon mas casos en la zona urbana')
print('---------------------------------------------------------')
        
print(casosP, casosN, casosF, casosm, casosM, casosA, casosR, casosU)
