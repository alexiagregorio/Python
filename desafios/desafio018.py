import math
angulo = float(input('Digite o ângulo que você deseja: '))
#S=O/H C=A/H T=O/A

seno = math.sin(math.radians(angulo)) #math.radians pra dar em angulo
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print('O ângulo de {} tem o SENO de {:.2f}, o COSSENO de {:.2f} e a TANGENTE de {:.2f}'.format(angulo, seno, cos, tan))

