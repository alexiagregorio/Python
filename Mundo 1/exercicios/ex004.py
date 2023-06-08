# n1 = input('Digite um número:')
# n2 = input('Digite outro número:')
# s = n1 + n2
# print('A soma dos números é', s) #o problema é que aqui só junta os dois números, concatena, ou seja 2 + 2 ele daria 22.

#PARA SOMAR VAMOS USAR O INT ou FLOAT:

n1 = float(input('Digite um número:'))
n2 = float(input('Digite mais um número:'))
soma = n1 + n2

#print('A soma dos números é', soma)
print('A soma entre {} e {} vale {}'.format(n1, n2, soma))
