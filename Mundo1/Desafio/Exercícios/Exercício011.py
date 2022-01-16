#Faça um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessárias para pintá-la, sabendo que cada litro de tinta, 
# pinta uma áea de 2m².

h=float(input('Digite a altura da parede: '))
l=float(input('Digite a largura da parede: '))
area=(h*l)
g=((area/2))

print('Uma parede de {:.2f} m² irá precisar de {:.2f} galão(ões) de Tinta.'.format(area, g))