#Crie um programa que Leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Considerar US$ 1.00 = R$ 3.27

d=float(input('Digite qual o valor você possui? \n'))

us= (d/3.27)

print('Com R$ {} você consegue comprar US$ {:.2f}.'.format(d, us))