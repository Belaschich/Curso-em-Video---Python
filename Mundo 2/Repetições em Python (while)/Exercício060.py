'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex:
5! = 5x4x3x2x1 = 120
'''
n = int(input('Digite um número para ver seu fatorial: '))
f = 1
num = n
while num > 0:
    f *= num
    num-=1
print(f'O Faorial do número {n} é: {f}')

