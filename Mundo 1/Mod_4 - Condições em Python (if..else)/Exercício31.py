'''
Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km de R$0,45 
para viagens mais longas.
'''
viagem = float(input("Quantos KM até o destino final? "))


if viagem > 200:
    valor = (viagem * 0.45)

else:    
    valor = (viagem * 0.50)

print("A Passagem custa R$ {}".format(valor))

