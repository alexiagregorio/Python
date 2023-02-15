frase = 'Curso em Vídeo Python '
print(frase.count('o')) #letras maiúsculas e minúsculas são diferentas
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
print(frase[0:23])
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.split())

dividido = frase.split()
print(dividido[0])
print(dividido[2] [3]) #pegou a segunda palavra e mostrou a 3 letra