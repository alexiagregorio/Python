n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro valor: '))
soma = n1 + n2
mult = n1 * n2
div = n1 / n2
divint = n1 // n2
expo = n1 ** n2
print('A soma é {}, \n o produto é {} e a \n divisão é {:.3f}'.format(soma, mult, div)) # o :.3f é para a divisão ter só 3 números depois da vírgula.
print('Divisão inteira {} e potência {}'.format(divint, expo))