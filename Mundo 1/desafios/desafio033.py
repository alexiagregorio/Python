#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o último valor: '))
#Verificando quem é o maior
if num1 > num2 and num1 > num3:
    print('O maior número é o {}'.format(num1))
if num2 > num1 and num2 > num3:
    print('O maior número é o {}'.format(num2))
if num3 > num1 and num3 > num2:
    print('O maior número é o {}'.format(num3))
#Verificando quem é o menor
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
print('O menor número foi {}'.format(menor))
