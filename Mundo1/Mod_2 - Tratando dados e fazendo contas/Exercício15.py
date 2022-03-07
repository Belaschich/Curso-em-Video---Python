# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
# e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

c=float(input('Quantos Km o carro percorreu?\n'))
d=int(input('Quantos dias o carro ficou alugado?\n'))

vkm= (c*0.15)
vd= (d*60)

t= (vkm+vd)

print('O carro ficou alugado por {} dias e rodou {}Km, o valor do aluguel foi de R${:.2f}'.format(d, c, t))
