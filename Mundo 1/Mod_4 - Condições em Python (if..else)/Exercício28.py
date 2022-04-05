'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e
peça para o usuario tentar descobrir qual foi o número escolhido pelo computador.

Obs. O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

from random import randint

cp = randint(0, 5)
print('-=-'*20)
print("Pensando em um número...")
print('-=-'*20)

us = int(input("Digite um número de 0 - 5: "))

if us == cp:
    print("Parabaéns! Você acertou!")
else:
    print("Não foi dessa Vez! O número sorteado foi {}, tente novamente".format(cp))
