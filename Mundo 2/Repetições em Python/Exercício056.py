'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, 
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''
from datetime import date
atual = date.today().year
contid = 0
idmaior = 0
nmaior = []
contsx = 0
for x in range (1, 5):
    print(f'----------------- Pessoa {x} -----------------')
    nome = input('Digite seu nome: ')
    idade = int(input('Digite a sua idade: '))
    sx = input('Digite seu genero F- Feminino, M- masculino: ').strip().upper()

    if idade > 0:
        contid +=idade
        md = contid/x
    
    if idade < 20 and sx == 'F':
        contsx +=1
    
    if idade > idmaior and sx =='M':
        idmaior = idade
        nmaior = nome
    else:
        print('Nenhum Homem no Grupo')

print(f'A média de idade do grupo é {md}')
print(f'O homem mais velho tem {idmaior} anos e se chama: {nmaior}')
print(f'No grupo existem {contsx} mulheres com menos de 20 anos') 

        

    
        


