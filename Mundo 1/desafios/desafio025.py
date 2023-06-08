#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite um nome: '))
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))