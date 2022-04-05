'''
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes
'''
r1 = float(input("Digite um valor: "))
r2 = float(input("Digite um Valor: "))
r3 = float(input("Digite um Valor: "))

if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    if
    print("Os valores {}, {} e {} podem formar um triângulo".format(r1, r2, r3))
else:
    print("Os valores {}, {} e {} não podem formar um triângulo".format(r1, r2, r3))