import random
import os
import time
cont = 0
print('''
                            /=====================================/
                            /Seja bem vindo ao jogo da adivinhação/
                            /=====================================/

O computador vai pensar num número de 0 a 10, e, enquanto você não acertar, ficará preso no jogo
''')

time.sleep(3)
for c in range(1,10):
    time.sleep(0.5)
    print()

print('O computador está pensando em um número, será que você consegue adivinhar???\n')
computador = random.randint(0,10)
n = int(input('Digite um número de 0 a 10: '))

while n != computador:
    cont += 1
    n = int(input('Você errou, tente novamente HAHAHAHA\nDigite outro número: '))
    if cont == 5:
        print('Isso vai ser infinito HAHAHAHA')

if cont == 0:
    print('Droga, fui derrotado, você não errou nenhuma vez')
else:
    print(f'Ah não, fui derrotado, mas você errou {cont} vezes')
