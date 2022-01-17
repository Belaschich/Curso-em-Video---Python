#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua Tabuada.

num= int(input('Digite um número para mostrar sua tabuada: '))

print('Tabuada do número {}\n'.format(num),
      '{} X {:2} = {:2}\n'.format(num, 1, num*1),
      '{} X {:2} = {:2}\n'.format(num, 2, num*2),
      '{} X {:2} = {:2}\n'.format(num, 3, num*3),
      '{} X {:2} = {:2}\n'.format(num, 4, num*4),
      '{} X {:2} = {:2}\n'.format(num, 5, num*5),
      '{} X {:2} = {:2}\n'.format(num, 6, num*6),
      '{} X {:2} = {:2}\n'.format(num, 7, num*7),
      '{} X {:2} = {:2}\n'.format(num, 8, num*8),
      '{} X {:2} = {:2}\n'.format(num, 9, num*9),
      '{} X {:2} = {:2}\n'.format(num, 10, num*10)
      )