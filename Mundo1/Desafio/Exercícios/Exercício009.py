#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua Tabuada.

num= int(input('Digite um número inteiro: '))

print('Tabuada do número {}\n'.format(num), 
      '{} X 1 = {}\n'.format(num, num),
      '{} X 2 = {}\n'.format(num, num*2),
      '{} X 3 = {}\n'.format(num, num*3),
      '{} X 4 = {}\n'.format(num, num*4),
      '{} X 5 = {}\n'.format(num, num*5),
      '{} X 6 = {}\n'.format(num, num*6),
      '{} X 7 = {}\n'.format(num, num*7),
      '{} X 8 = {}\n'.format(num, num*8),
      '{} X 9 = {}\n'.format(num, num*9),
      '{} X 10 = {}\n'.format(num, num*10))