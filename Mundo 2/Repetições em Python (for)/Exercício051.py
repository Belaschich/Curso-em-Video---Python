'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''
pt = int(input('Digite um número inteiro: '))
r = int(input('Digite a razão para a PA: '))


for x in range (1, 10):
    print(pt)
    pt+=r
print(pt)


''' ----------------------------FORMA DO GUANABARA-------------------------------------'''

pt = int(input('Digite um número inteiro: '))
r = int(input('Digite a razão para a PA: '))
d = pt + (10 -1) * r

for x in range (pt, d + r, r):
    print('{}'.format(x), end = ' --> ')
print('Fim')
