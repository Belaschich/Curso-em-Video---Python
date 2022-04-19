'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''

n = int(input('Digite um número inteiro: '))

mult = 0

for x in range (2, n):
    if (n % x == 0):
        print(f'multiplo de {x}')
        mult +=1
if (mult == 0):
    print('É primo!')
else:
    print('Não é primo!')