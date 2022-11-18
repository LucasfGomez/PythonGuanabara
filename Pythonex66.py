#Ler vários números e somalos
from os import system
n = int(input('Informe o número que quer adicionar à somatória: '))
c = 0
cont = 0
while True:
    if n == 999:
        break
    else:
        system('cls')
        print(f'{n} adcionado à somatória')
        c += n
        cont += 1
        n = int(input('Informe o número que quer adicionar à somatória\nCaso não queira adicionar número, digite [999]: '))
system('cls')
print(f'A soma dos {cont} números digitados é: {c}')