'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''

from ctypes.wintypes import VARIANT_BOOL


valor_casa= float(input('Qual o valor da casa?   R$' ))
sal= float(input('Qual o seu salário?  R$'))
anos= int(input("Em quantos anos pretende quitar? "))

prest= (valor_casa/(anos*12))
sal_porcento= (sal*0.3)

if prest >= sal_porcento:
    print("Para pagar um imóvel de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}. Empréstimo NEGADO!".format(valor_casa, anos, prest))

else: 
    print("Para pagar um imóvel de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}. Parabéns!!! Emprestimo aprovado!".format(valor_casa, anos, prest)) 

