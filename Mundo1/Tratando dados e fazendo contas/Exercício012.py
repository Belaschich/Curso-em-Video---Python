#Faça uam algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p=float(input('Digite o valor do produto: R$ '))
d=(p-(p*(5/100)))

print('O valor final do produto com desconto é: R${:.2f}'.format(d))