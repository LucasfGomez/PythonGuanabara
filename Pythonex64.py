#Ler vários números e somalos
from os import system
n = int(input('Informe o número que quer adicionar à somatória: '))
c = 0
while n !=999:
    system('cls')
    print(f'{n} adcionado à somatória')
    c += n
    n = int(input('Informe o número que quer adicionar à somatória\nCaso não queira adicionar número, digite [999]: '))
system('cls')
print(f'O resultado da somatória dos números digitador é {c}')