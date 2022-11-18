import os
pri=int(input('Digite o primeiro valor!\n'))
seg=int(input('Digite o segundo valor!\n'))
ter=int(input('Digite o terceiro valor!\n'))
lista=[pri,seg,ter]
os.system('cls')
print('Você digitou os seguintes números: ',lista)
lista.sort()
print('O menor valor é {} e o maior valor é {}'.format(lista[0],lista[-1]))