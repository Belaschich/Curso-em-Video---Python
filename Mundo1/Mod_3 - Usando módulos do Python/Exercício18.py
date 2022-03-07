#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

n= float(input('Digite o valor do ângulo: '))
s= math.sin(math.radians(n))
c= math.cos(math.radians(n))
t= math.tan(math.radians(n))
print('O Seno do ângulo de {} graus é {:.2f}\n'.format(n, s),
      'O Cosseno do ângulo de {} graus é {:.2f}\n'.format(n, c),
      'A tangente do ângulo de {} graus é {:.2f}'.format(n, t)
)