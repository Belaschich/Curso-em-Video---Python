'''
Escreva um programa que pergunte  salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.

Para os inferiores ou iguais o aumento é de 15%.
'''

sal = float(input("Digite seu salário: "))

if sal > 1250:
    new = ((sal*10/100) + sal)
    print("Você teve um aumento de 10% e seu salário foi para R$ {}".format(new))

else:
    new = ((sal*15/100) + sal)
    print("Você teve um aumento de 15% e seu salário foi para R$ {}".format(new))


