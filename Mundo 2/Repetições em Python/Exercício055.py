'''
Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos.
'''
kgmaior = 0
kgmenor = 0
for x in range (1,6):
    peso = float(input('Digite o peso da pessoa {}: '.format(x)))
    
    if x == 1:
        kgmaior = peso
        kgmenor = peso
    else:
        if peso > kgmaior:
            kgmaior = peso
        if peso < kgmenor:
            kgmenor = peso
    
print(f'O maior peso é de {kgmaior} kg e o menor é de {kgmenor} kg')