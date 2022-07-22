'''
Faça um programa que calcule a soma entre todos os números que são múltiplos de três 
e que se encontram no intervalo de 1 até 500.
'''
soma = 0
cont = 0
for x in range(1, 501, 2):
    if x % 3 ==0:
        soma +=x
        cont +=1
print(f'Entre 1 e 500 existem {cont} números multiplos de 3 e a soma deles é {soma}')
