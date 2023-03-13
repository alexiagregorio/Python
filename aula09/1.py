##############################################

'''              TIPOS DE FATIAMENTO:
frase: Curso em Vídeo Python

frase[9] mostra só a 9 casa da frase, ou seja o "V"

frase[9:13] mostra da 9° casa até a 12°, não vai até o 13, fica uma antes

frase[9:21:2] vai da 9° casa até a 20° pulando de 2 em 2 (V, d, o, P, t, o)

frase[:5] começa do caractere 0 até o 5°

frase[15:] começa do 15 até o final

frase[9::3] começa no 9 até o final pulando de 3 em 3

len(frase) - mostra a length da frase, ou seja 21 caracteres 

frase.count('o') - pediu para contar quantas vezes a letrs 'o' aparece

frase.count('o', 0, 13) - vai contar de 0 a 13 quantas letras 'o' tem

frase.find('deo') - mostra quantas vezes ele encontrou 'deo' e em quais posições

frase.find('Android') - como não existe essa string na frase ele vai te retornar com o valor -1

'Curso' in frase - o operador 'in' pergunta se existe essa palavra na string, se for real ele retorna com 'True'
'''

##############################################
'''               TRANSFORMAÇÃO

frase.replace('Python','Android') - substitui a palavra python por android na string

frase.upper() - upper é um método por isso usamos (), isso vai deixar todas as letras que estavam minúsculas em maiúsculas

frase.lower() - deixa tudo em minúsculo

frase.capitalize() - coloca tudo em minúsculo, só a primeira letra fica maiúscula

frase.title() - analisa quantas palavras tem na frase e deixa todas as palavras com a primeira letra maiúscula. "Curso Em Vídeo Python"

frase.strip() - remove todos os espaços inúteis no começo e no final da string

frase.rstrip() - remove os espaços do lado direito

frase.lstrip() - remove os espaços da esquerda                '''

##############################################

'''                  DIVISÃO

frase.split() - ocorre uma divisão considerando os espaços. Divide uma string em uma lista
Ex: Curso | em | Vídeo | Python
    01234   01   01234   012345
    
'-'.join(frase) - gera uma string única assim:
Curso-em-Vídeo-Python

'''