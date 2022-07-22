'''
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites 
foram necessários para vencer.
'''

from random import randint
palpite = 0
cp = randint(0, 10)
print('-=-'*20)
print("Pensando em um número...")
print('-=-'*20)

us = int(input("Digite um número de 0 - 10: "))

while us != cp:
    print("Não foi dessa Vez! Tente novamente".format(cp))
    palpite +=1
    us = int(input("Digite um número de 0 - 10: "))
print("Parabaéns! Você acertou!")
if palpite == 1:
    print(f'Até acertar você tentou {palpite} veze.')
else:    
    print(f'Até acertar você tentou {palpite} vezes.')




