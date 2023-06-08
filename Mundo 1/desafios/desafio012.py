p = float(input('Qual o preço do produto? R$'))

#Desconto de 5% --> 0,5
d = (p * 5) / 100  #desconto
novo = p - d       #novo preço

print('O produto que custava R${:.2f}, na promoção ganhou um desconto de R${:.2f} e o novo valor do produto é de R${:.2f}'.format(p, d, novo))