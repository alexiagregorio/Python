# \033[0;33;44m
# \033[style;text;backgroundm

#0 none
#1 bold
#4 underline
#7 negative

# 30 -> branco| 31-> vermelho| 32-> verde| 33-> amarelo| 34-> azul| 35-> roxo| 36 -> ciano| 37-> cinza (TEXT)
#      40     |      41      |     42    |      43     |    44    |   45     |     46     |     47     (BACKGROUND)

#PARA LETRA PRETA É NUMERO 7, ex: \033[7;30m       fica letra preta com fundo branco, O SETE(7) INVERTE AS CORES!

print('\033[7;33;44mOlá, Mundo!\033[m')

a = 3
b = 5

print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a,b))

nome = 'Alexia'
print('Olá! Muito prazer em te conhecer {}{}{}!'.format('\033[4;45m', nome, '\033[m'))

nome1 = 'Gustavo'
cores = {
    'limpa':'\033[m',
    'azul':'\033[34m',
    'amarelo':'\033[33m',
    'pretoebranco':'\033[7;30m'
}
print('Olá, Muito prazer em te conhecer, {}{}{}!'.format(cores['amarelo'], nome1, cores['limpa']))
