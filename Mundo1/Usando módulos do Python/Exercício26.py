#Faça um programa  que leia  uma afrase pelo teclado  e mostre:
#- Quantas vezes aparece a letra "A"
#- Em que posição ela aparece a primeira vez
#- Em que posição ela aparece a ultima vez

f = str(input('Digite uma frase:')).upper().strip()

a = f.count('A')
a1= f.find('A') + 1
a0= f.rfind('A') + 1

#função rfind(), é usada para achar a última posição da letra ou palavra buscada

print('A letra "A" aparece {} vezes na frase\n'
      'Está na posição {} pela primeira vez\n'
      'E aparece na posição {} pela última vez'.format(a, a1, a0))