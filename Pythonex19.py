import random
a1 = input('Primeiro aluno\n')
a2 = input('Segundo aluno\n')
a3 = input('Terceiro aluno\n')
a4 = input('Quarto aluno\n')
lista = [a1,a2,a3,a4] #Em Python, listas ficam entre []
sort = random.choice(lista)
print('O Aluno {} foi o escolhido'.format(sort))