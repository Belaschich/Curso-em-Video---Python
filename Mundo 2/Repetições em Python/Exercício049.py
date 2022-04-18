'''
Refaça o DESAFIO 9, 
mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''

num= int(input('Digite um número para mostrar sua tabuada: '))

for x in range(0, 11):
    print(f'{num:2} x {x:2} = {num*x:2}')






