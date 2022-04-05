'''
faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''

ano = int(input("Digite um ano e veja se ele é Bissexto ou não: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400:
    print("O ano de {} é Bissexto".format(ano))
else:
    print("O ano de {} não é Bissexto".format(ano))