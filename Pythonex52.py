from colorama import Fore, Back, Style
from os import system
system('cls')
n = int(input('Digite o número que você quer descobrir se é primo\n'))
cont=0
for c in range(1,n+1):
    if n % c == 0:
        print(Fore.GREEN,end='')
        print(c,end=' '+Style.RESET_ALL)
        cont += 1
    else:
        print(c,end=' ')
if cont == 2:
    print(f'\nO número {n} foi dividido {cont} vezes, portanto, É PRIMO')
else:
    print(f'\nO número {n} foi dividido {cont} vezes, portanto, NÃO É PRIMO')
