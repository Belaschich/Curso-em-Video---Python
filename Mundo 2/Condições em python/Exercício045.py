'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''

import random
Pedra = 1
Papel = 2
Tesoura = 3

jogador= int(input("Escolha entre: \n" 
    "1- Pedra \n" 
    "2- Papel \n" 
    "3- Tesoura \n" ))

pc = [1, 2, 3]

jogo = random.choice(pc)

if jogador == jogo:
    print("O computador jogou {} e você  {}, nulo".format(jogo, jogador))
elif jogador == 1 and jogo == 3:
    print("O computador jogou {} e você  {}, Você Ganhou!!!".format(jogo, jogador))
elif jogador == 2 and jogo == 3:
    print("O computador jogou {} e você  {}, O Computador Ganhou!!!".format(jogo, jogador))
else:
    print("O computador jogou {} e você  {}, Você Ganhou!!!".format(jogo, jogador))
