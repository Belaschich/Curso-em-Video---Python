#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo 
# e todas as informações possíveis sobre ele.

x=input('Digite qualquer coisa...: ')

print('É um alphanumerico?', x.isalnum())
print('É um alpha?', x.isalpha()) 
print('É um número decimal?', x.isdecimal()) 
print('Está em letra Minúscula?', x.islower())
print('É um numérico?', x.isnumeric())
print('Tem espaço?', x.isspace())
print('É um Título?', x.istitle()) 
print('está em capslock?', x.isupper()) 
print('É uma subclasse?', x.__init_subclass__())
print('O Tipo primitivo é, ', type(x))