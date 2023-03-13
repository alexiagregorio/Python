#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome de uma cidade: ')).strip()
print(cidade[0:5].upper() == 'SANTO') #usa o upper pra jogar tudo em maiúscula e não ter problema se for escrito com maiúscula ou minúscula