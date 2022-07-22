'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida
'''
peso= float(input("Qual o seu peso? "))
h= float(input("Qual a sua altura? "))

imc = (peso/(h*h))

if imc < 18.5:
    print("Seu IMC (Indice de Massa Corporea) é {:.2f}, você está Abaixo do Peso".format(imc))
elif imc >= 18.5 and imc < 25:
    print("Seu IMC (Indice de Massa Corporea) é {:.2f}, você está com o Peso Ideal".format(imc))
elif imc >= 25 and imc < 30:
    print("Seu IMC (Indice de Massa Corporea) é {:.2f}, você está com Sobrepeso".format(imc))
elif imc >= 30 and imc < 40:
    print("Seu IMC (Indice de Massa Corporea) é {:.2f}, você está com Obesidade".format(imc))
else:
    print("Seu IMC (Indice de Massa Corporea) é {:.2f}, você está com Obesidade Mórbida".format(imc))
