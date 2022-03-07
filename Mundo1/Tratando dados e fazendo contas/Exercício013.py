#Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s=float(input('Digite o salário: R$ '))

ns=(s+(s*(15/100)))

print('Seu salário teve um acréscimo de 15% e foi de R${:.2f} para R${:.2f}.'.format(s, ns))