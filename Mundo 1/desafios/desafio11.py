l = float(input('Digite a largura da sua parede: '))
alt = float(input('Digite a altura da sua parede: '))
# Área = base x altura

a = l * alt
litro = a / 2 

print('Considerando que um litro de tinta pinta uma área de 2m²: \nA sua área é de {}m² \nVocê precisará de {} litros de tinta.'.format(a, litro))


