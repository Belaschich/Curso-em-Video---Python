'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
 desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO,
ANOTARAM A DATA DA MARATONA.
'''
f = str(input('Digite uma frase: ')).strip().upper()
p= f.split()
j= ''.join(p)
i=''

for x in range (len(j) -1, -1, -1):
    i += j[x]

if i == j:
    print('Políndromo')

else:
    print('Não é Políndromo')

'''------------------------------ OUTRA FORMA SEM UTILIZAR O FOR--------------------------------'''

f = str(input('Digite uma frase: ')).strip().upper()
p= f.split()
j= ''.join(p)
i = j[::-1]

if i == j:
    print('Palíndromo')

else:
    print('Não é Palíndromo')