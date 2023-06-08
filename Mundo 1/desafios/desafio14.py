c = float(input('Informe a temperatura em °C: '))
# 1°C ----- 33.8°F
# temp ---- f
f = ((c * 9)/5) + 32  #essa é a formula para passar de °C para °F

print('A temperatura {}°C equivale a {:.1f}°F'.format(c, f))