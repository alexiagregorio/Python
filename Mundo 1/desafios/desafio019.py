import random
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Nome do segundo aluno: ')
aluno3 = input('Nome do terceiro aluno: ')
aluno4 = input('Nome do quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4] #para python uma lista fica entre colchetes
escolhido = random.choice(lista)
print('O aluno sorteado foi: {}'.format(escolhido))