#Ler vários números e somalos
from os import system
n = int(input('Informe o número que quer adicionar à somatória: '))
c = 0
maior = 0
menor = 9999
media = 0
cont = 0
conti = 'u'
while n != 0:
    system('cls')
    print(f'{n} adcionado à somatória')
    c += n
    cont +=1
    if n < menor:
        menor = n
    elif n > maior:
        maior = n
    media = c / cont
    n = int(input('Caso queria parar, digite [0]\nSe não informe o número que quer adicionar à somatória: '))
system('cls')
print(f'O resultado da somatória dos números digitador é {c} e a média é {media}')
print(f'O maior número foi {maior} e o menor foi {menor}')