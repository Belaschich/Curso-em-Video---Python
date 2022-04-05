'''
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais
'''
x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))

if x > y:
    print("O primeiro número ({}) é de maior valor".format(x))

elif y > x:
     print("O segundo número ({}) é de maior valor".format(y))

else:
    print("Não existe valor maior, os dois são iguais")