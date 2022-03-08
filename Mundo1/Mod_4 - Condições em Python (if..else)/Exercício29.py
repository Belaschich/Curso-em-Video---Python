'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.

A multa vai custara R$7a por cada KM acima do limite
'''

v = float(input("Digite a velocidade do carro: "))

km = 0

if v > 80.0:
    km = (v  - 80.0)
    valor = (km * 7)
    print("MULTADO!! Você ultrapassou o limte de 80km/h e recebeu uma multa no valor de R$ {}".format(valor))    

else: 
    print("Parabéns Continue assim!")

