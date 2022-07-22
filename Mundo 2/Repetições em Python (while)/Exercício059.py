'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''

v1 = int(input('Digite um número inteiro: '))
v2 = int(input('\nDigite um número inteiro: '))
menu = int(input('\nQual operação você gostaria de realizar:\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\n'))


while menu == 1 or menu == 2 or menu == 3 or menu == 4 or menu == 5:
    if menu == 1:
        somar = v1 + v2
        print(f'A soma dos números digitados é: {somar}\n')
        print('Vamos novamente')
        menu = int(input('\nQual operação você gostaria de realizar:\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\n'))

    if menu == 2:
        mult= v1 * v2
        print(f'A multiplicação dos números digitados é: {mult}\n')
        print('Vamos novamente')
        menu = int(input('\nQual operação você gostaria de realizar:\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\n'))

    if menu == 3:
        if v1 > v2:
            print(f'O maior número digitado é {v1}\n')
        elif v1 < v2:
            print(f'O maior número digitado é {v2}\n')
        else:                
            print('Os Números são iguais\n')
        print('Vamos novamente')
        menu = int(input('\nQual operação você gostaria de realizar:\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\n'))

    if menu == 4:
        v1 = int(input('Digite um número inteiro: '))
        v2 = int(input('\nDigite um número inteiro: '))
        print('Vamos novamente')
        menu = int(input('\nQual operação você gostaria de realizar:\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\n'))
    
    if  menu == 5: 
        print('Tchau até outra hora!')
        break
    
    while menu != 1 and menu != 2 and menu != 3 and menu != 4 and menu != 5:
        print('Opção inválida!')    
        print('Vamos novamente')
        menu = int(input('\nQual operação você gostaria de realizar:\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\n'))
    
    
