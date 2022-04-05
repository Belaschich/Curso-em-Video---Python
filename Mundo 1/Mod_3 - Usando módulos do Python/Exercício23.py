#Faça um programa  que leia um número de 0 a 9999 e mostre na tela cada 
# um dos dígitos separados. Obs. Unidade, Dezena, centena e milhar

n = int(input('Digite um número de 0 até 9999: '))

U = n //1 %10
D = n //10 %10
C = n //100 %10
M = n //1000 %10

print('Unidade: {}\n'
      'Dezena: {}\n'
      'Centena: {}\n'
      'Milhar: {}'.format(U, D, C, M))