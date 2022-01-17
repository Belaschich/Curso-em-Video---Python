#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa.

import math

co=float(input('Digite o valor do Cateto Oposto: '))
ca=float(input('Digite o valor do Cateto Adjacente: '))
h=math.hypot(co, ca)

print('O Valor da Hipotenusa é: {:.2f}'.format(h))