'''
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerra quando ele disser que  quer mostrar 0 termos.
'''

pt = int(input('Digite um número inteiro: '))
r = int(input('Digite a razão para a PA: '))
cont = 1
t = 0
mais = 10

while mais != 0:
    t += mais
    while cont <= t:
        print(f'{pt} ->', end= '')
        pt+=r
        cont +=1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Foram mostrados {t} termos no total')

