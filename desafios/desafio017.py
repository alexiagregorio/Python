'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente:'))

h = (co ** 2 + ca ** 2) ** (1/2) #esse ** (1/2) serve pra fazer a raiz quadrada 
# h² = co² + ca²

print('A hipotenusa vai medir {:.2f}'.format(h))'''

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente:'))
h = math.hypot(co, ca) #muito mais fácil

print('A hipotenusa é de {:.2f}'.format(h))