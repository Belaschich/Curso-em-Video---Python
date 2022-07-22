'''
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
print('=-='*10, 'Vamos brincar com os numeros!!', '=-='*10)

tx = input('Você gostaria de saber a média dos valores digitados? [S/N] ').upper()

if tx != 'S' and tx != 'N':
    print('Não entendi!')
    tx = input('Você gostaria de saber a média dos valores digitados? [S/N] ').upper()


soma = 0
cont = 0
maior = 0
menor = 0

while tx == 'S':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1     
    if maior == 0 and menor == 0:
        menor = n
        maior = n    
    elif maior <= n:
        maior = n
    elif menor >= n:
        menor = n
    tx = input('Você gostaria de continuar a digitar os valores? [S/N] ').upper()
    if tx != 'S' and tx != 'N':
        print('Não entendi!')
   
        tx = input('Você gostaria de continuar a digitar os valores? [S/N] ').upper()
media = (soma/cont)
print(f'A média dos números digitados é: {media}, o maior número digitado foi {maior} e o menor foi {menor}.')

'''
if tx == 'N':
    media = (soma/cont)
    print(f'A média dos números digitados é: {media}, o maior número digitado foi {maior} e o menor foi {menor}.')'''