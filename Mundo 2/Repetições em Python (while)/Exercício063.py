'''
Escreva um programa que leia um numero "n" inteiro qualquer e mostre na tela os "n" 
primeiros elementos de uma Sequencial de Fibonacci

Ex:
0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
'''

n = int(input('Digite um número inteiro: '))
cont= 0
next = 0

while next < n+1: 
    print('{}'.format(next), end =' -> ')   
    next = next + cont
    cont = next - cont
    if next == 0:
        next +=1
print('Fim')   
