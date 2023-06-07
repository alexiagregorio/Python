#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR
numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2 #todo numero par vqai dar o resultado 0, e todo numero impar vai dar resultado 1
if resultado == 0:
    print('O número {} é par!'.format(numero))
else:
    print('O número {} é ímpar!'.format(numero))