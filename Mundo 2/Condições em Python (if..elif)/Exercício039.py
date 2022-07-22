'''
Faça um programa que leia o ano de nascimento de um jovem e informe, 
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

ano_nasc= int(input("Digite seu ano de nascimento: "))
ano_atual= 2022
idade = (ano_atual - ano_nasc)
dif = 0
if idade > 18:
    dif = idade - 18
    if dif >1:
        print("OPA! Já passou {} anos do tempo de alistamento".format(dif))
    else:
        print("OPA! Já passou {} ano do tempo de alistamento".format(dif))

elif idade < 18:
    dif = 18 - idade
    if dif > 1:
        print("Xiii! Faltam {} anos para se alistar".format(dif))
    else:
        print("Xiii! Falta {} anos para se alistar".format(dif))
else:
    print("ESTÁ NA HORA!!! Esse é o ano do seu alistamento!!")



