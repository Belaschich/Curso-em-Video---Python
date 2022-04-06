'''
Escreva um programa em Python que leia um número inteiro qualquer e peça para 
o usuário escolher qual será a base de conversão: 
1 para binário, 2 para octal e 3 para hexadecimal.
'''

n= int(input("Digite um número qualquer: "))

menu= int(input('''Qual base de conversão, gostaria de usar? 
            1- binário
            2- octal 
            3- hexadecimal
            Opção: '''))

if menu == 1:
    print("O número digitado {} em Binário é {}".format(n, bin(n)[2:]))
elif menu == 2:
    print("O número digitado {} em Octal é {}".format(n, oct(n)[2:]))
elif menu == 3:
    print("O número digitado {} em Octal é {}".format(n, hex(n)[2:]))
else:
    print("Menu inválido, tente novamente!")
