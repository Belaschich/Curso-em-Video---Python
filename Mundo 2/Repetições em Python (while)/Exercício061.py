'''
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, 
mostrando os 10 primeiros termos da proogressão usando a estrutura while.
'''

pt = int(input('Digite um número inteiro: '))
r = int(input('Digite a razão para a PA: '))
cont = 1

while cont <= 10:
    print(f'{pt} ->', end= '')
    pt+=r
    cont +=1
print('FIM')


