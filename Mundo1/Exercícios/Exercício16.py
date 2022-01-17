#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
n= float(input('Digite um número real: '))
i= math.trunc(n)
print('O número digitado na sua forma inteira é: {}'.format(i))