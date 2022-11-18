from time import sleep
from os import system
tab =  int(input('Você quer saber a tabuada de que número?\n'))
system('cls')
print('Calculando...')
sleep(2)
for c in range(0,11):
    print('{} x {} = {}'.format(tab, c, (tab*c)))
