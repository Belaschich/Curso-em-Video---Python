#Escreva um programa que converta uma temperatura digitada em C e converta para F.

C=float(input('Digite o valor da temperatura em celsius: '))
F= ((9*C)/5+32)

print('A temperatura {}c está como {}f.'.format(C, F))