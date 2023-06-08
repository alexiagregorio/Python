#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar desconbrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
computador = randint(0, 5) #aqui o computador sorteia
print('Voun pensar em um número entre 0 e 10. Tente adivinhar...')
jogador = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar
print('Processando...')
sleep(2)
if jogador == computador:
    print('Parabéns! Você acertou!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(computador, jogador))