import random
import os
import time
'''print(Sejá bem vindo ao jogo!!
O computador irá pensar em um número\nE você deve adinhar que número ele escolheu)
nmr = int(input(('Escolha o número que você acha que o computador escolheu\n')))
pc=random.randint(0,5)
os.system('cls')
print('O computador escolheu -=({})=-'.format(pc))
if nmr == pc:
    print('Você acertou')
else:
    print('Você errou')
#O de cima fui eu e o de baixo foi o Guanaba'''
computador = random.randint(0,5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?\n'))
print('PROCESSANDO...')
time.sleep(3)
if jogador == computador:
    print('PARABÉNS! Você me venceu!')
else:
    print('GANHEI! Eu pensei no número {} e não no número {}'.format(computador,jogador))