nome = str(input('Digite seu nome completo: '))
print('Seu nome em maiúsculas é {}'.format(nome.upper())) #nome com todas as letras maiusculas
print('Seu nome em minúsculas é {}'.format(nome.lower())) #Nome com todas as letras minusculas
print(len(nome)) #quantos caracteres ao todo
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' '))) #quantas letras ao todo sem considerar os espaços

#####QUANTAS LETRAS TEM O PRIMEIRO NOME - não consegui#######
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))