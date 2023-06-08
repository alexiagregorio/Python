dias = float(input('Quantos dias alugado? '))
km = float(input('Quantos Km rodados? '))

pd = dias * 60 
pk = km * 0.15
total = pd + pk

print('O total a pagar é de R${:.2f}'.format(total))