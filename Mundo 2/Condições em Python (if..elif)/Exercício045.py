'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''

import random

jogador= input("Escolha entre: \n" 
    "Pedra \n" 
    "Papel \n" 
    "Tesoura \n" ).upper().strip()

pc = ('PEDRA', 'PAPEL', 'TESOURA')

jogo = random.choice(pc)

if jogo == jogador:
    print("O computador jogou {} e você  {}, Empete!".format(jogo, jogador))
elif jogo == 'PEDRA' and jogador == 'TESOURA':
    print("O computador jogou {} e você  {}, O Computador Ganhou!!!".format(jogo, jogador))
elif jogo == 'TESOURA' and jogador == 'PAPEL':
    print("O computador jogou {} e você  {}, O Computador Ganhou!!!".format(jogo, jogador))
elif jogo == 'PAPEL' and jogador == 'PEDRA':
    print("O computador jogou {} e você  {}, O Computador Ganhou!!!".format(jogo, jogador))
else:
    print("O computador jogou {} e você  {}, Você Ganhou!!!".format(jogo, jogador))
