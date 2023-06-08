num = float(input('Digite um número: '))

d = num * 2
t = num * 3
raiz = pow(num, 1/2) # calcula a raiz, também dava pra fazer => num ** (1/2)

print('O dobro de {} é {}, \n o triplo é {}, \n e a raiz quadrada é {:.2f}.'.format(num, d, t, raiz))