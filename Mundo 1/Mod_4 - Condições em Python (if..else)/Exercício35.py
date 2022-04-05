'''
Desenvolva  um programa que leia o comprimento de três retas 
e diga ao usuário se elas podem ou não formar um triângulo.
'''	

r1 = float(input("Digite um valor: "))
r2 = float(input("Digite um Valor: "))
r3 = float(input("Digite um Valor: "))

if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print("Os valores {}, {} e {} podem formar um triângulo".format(r1, r2, r3))
else:
    print("Os valores {}, {} e {} não podem formar um triângulo".format(r1, r2, r3))