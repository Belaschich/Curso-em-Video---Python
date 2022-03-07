#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.



nome = str(input('Digite seu nome completo:'))
nome_minusculo = nome.lower()
nome_maiusculo = nome.upper()
total_letras = nome.split()
total_letras = len(total_letras[0] + total_letras[1])
primeiro_nome = nome.split()
primeiro_nome = len(primeiro_nome[0])

print("Nome maiusculo: {} \n"
      "Nome minusculo: {} \n" 
      "Total de letras: {}\n"
      "Primeiro nome tem {} letras.".format(nome_maiusculo, nome_minusculo, total_letras, primeiro_nome))


