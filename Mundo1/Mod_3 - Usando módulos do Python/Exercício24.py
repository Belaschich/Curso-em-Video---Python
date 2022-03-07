#Crie um progama que leia o nome de uma cidade e diga se ela começa ou não 
# com o nome "Santo"

c = input('Digite o nome de uma cidade:')
c = c.title().split()
pl = c[0]
print('Santo' in pl)
