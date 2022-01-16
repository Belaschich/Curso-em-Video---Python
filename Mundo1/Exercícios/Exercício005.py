#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n= int(input('Digite um número inteiro: '))
ant= (n-1)
su= (n+1)

print('O antecessor de {} é {} e seu sucessor é {}.'.format(n, ant, su))

