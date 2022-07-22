'''
Faça um programa que leia o sexo de uma pessoas, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter o valor correto.
'''


sexo = input('Digite seu sexo [M/F]: ').upper()

while sexo != 'M' and sexo != 'F':
        print('Ops! Opção errada, tente novamente!')
        sexo = input('Digite seu sexo [M/F]: ').upper()
print(f'Seu gênero é : {sexo}')

    


    

