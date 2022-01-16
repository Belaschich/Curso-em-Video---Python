#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

m= float(input("Digite um valor: "))
cm= (m*100)
mm= (m*1000)

print('O valor digitado seria de {} metros, o mesmo valor em centímetros é: {}, e em milímetros é: {}'.format(m, cm, mm))