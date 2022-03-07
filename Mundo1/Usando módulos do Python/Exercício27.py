#Faça um programa que leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro e o ultimo nome  separadamente.
#Exp. Ana Maria  de Souza
#Primeiro = Ana
#último - Souza

nc = input('Digite um nome completo:')
lista = nc.split()

P = lista[0]
U = lista[-1]

print('Primeiro nome é:{}\n'
      'Último nome é:{}'.format(P,U))