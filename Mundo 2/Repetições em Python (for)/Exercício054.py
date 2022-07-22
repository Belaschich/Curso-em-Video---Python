'''
Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
from datetime import date
atual = date.today().year 
contmaior = 0
contmenor = 0

for x in range(0, 7):
    nasc = int(input('Digite o ano do seu nascimento: '))
    id =   atual - nasc
    if id >= 21:
        contmaior +=1
    else:
        contmenor +=1
print(f'{contmaior} pessoas são maior de idade e {contmenor} pessoas não menor de idade.') 

