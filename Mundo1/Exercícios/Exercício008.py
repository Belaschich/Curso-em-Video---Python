#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

m= float(input("Digite um valor: "))
cm= (m*100)
mm= (m*1000)

#print('O valor digitado seria de {} metros, o mesmo valor em centímetros é: {}, e em milímetros é: {}'.format(m, cm, mm))

#Na correção foi pedido para fazer todas as medidas.

km=(m/1000)
hm=(m/100) 
dam=(m/10)
dm=(m*10)

print('A medida dada foi {} metros, e a mesma foi convertida às medidas abaixo: \n'.format(m),
    'km= {}\n'.format(km),
    'hm= {}\n'.format(hm),
    'dam= {}\n'.format(dam),
    'm= {}\n'.format(m),
    'dm= {:.2f}\n'.format(dm),
    'cm= {:.2f}\n'.format(cm),
    'mm= {:.2f}\n'.format(mm)
     )