s = float(input('Qual o salário do funcionário? R$'))

a = s * 15 / 100
novo = s + a

print('O antigo salário era de R${:.2f}, o reajuste foi de 15% (R${:.2f}), o salário final é de R${:.2f}'.format(s, a, novo))