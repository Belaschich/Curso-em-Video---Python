'''
A Confederação Nacional de Natação precisa de um programa que leia 
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
'''

ano_nasc= int(input("Digite o ano do seu nascimento: "))
ano_atual= 2022

idade= (ano_atual - ano_nasc)

if idade <= 9:
    print("Você tem {} anos está na categoria MIRIM!".format(idade))
elif idade > 9 and idade <= 14:
    print("Você tem {} anos está na categoria INFANTIL!".format(idade))
elif idade > 14 and idade <= 19:
    print("Você tem {} anos está na categoria JÚNIOR!".format(idade))
elif idade > 19 and idade <= 25:
    print("Você tem {} anos está na categoria SÊNIOR!".format(idade))
else:
    print("Você tem {} anos está na categoria MASTER!".format(idade))
