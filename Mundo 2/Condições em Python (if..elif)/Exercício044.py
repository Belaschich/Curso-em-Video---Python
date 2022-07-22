'''
Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros
'''
valor = float(input("Qual o valor do produto? R$ "))

menu= int(input("Escolha a forma de pagamento: \n" 
    "1- À vista dinheiro/cheque: 10% de desconto \n" 
    "2- À vista no cartão: 5% de desconto \n" 
    "3- Em até 2x no cartão: preço formal \n" 
    "4- 3x ou mais no cartão: 20% de juros \n" ))

valor_desc_10= (valor - (valor*0.1))
valor_desc_5= (valor - (valor*0.05))
valor_juros= (valor + (valor*0.2))

if menu == 1:
    print("Valor do produto R$ {:.2f}, pagamento a vista dinheiro/cheque com desconto é R$ {:.2f}".format(valor, valor_desc_10))
elif menu == 2:    
    print("Valor do produto R$ {:.2f}, pagamento a vista cartão com desconto é R$ {:.2f}".format(valor, valor_desc_5))
elif menu == 3:    
    print("Valor do produto R$ {:.2f}, pagamento em até 2x no cartão sem juros".format(valor))
else:
    print("Valor do produto R$ {:.2f}, pagamento em até 2x no cartão é R$ {:.2f}".format(valor, valor_juros))


