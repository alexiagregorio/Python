#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

#Ex:
#Digite um número: 1834
#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1

num = int(input('Informe um número: '))
u = num // 1 % 10 #pego um numero divido por 1 e tiro o modulo de 10, ou seja o resto
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

####TINHA JEITO MAIS FÁCIL####
#num = int(input('Informe um número: '))
#n = str(num) - pq dai passa pra string

#print('Analisando o número {}'.format(num))
#print('Unidade: {}'.format(num[3]))
#print('Dezena: {}'.format(num[2]))
#print('Centena: {}'.format(num[1]))
#print('Milhar: {}'.format(num[0]))

#esse dava problema se o numero não tivesse as 4 casas, por ex: 123, ai daria erro pq não tem milhar