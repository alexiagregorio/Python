from math import trunc
num = float(input('Digite um número real qualquer para ver sua porção inteira: '))

#print('O número {} tem a parte inteira {}.'.format(num, math.floor(num)))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))