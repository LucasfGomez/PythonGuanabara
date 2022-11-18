from random import randint
from os import system
from time import sleep

print(f'{"Par ou Impar, vamos jogar?":-^30}')
sleep(1)
system('cls')
cont = 0
vitoriacomp = 0
co = 'S'
#JOGO EM SI
while co == 'S':
    while True:
        #DECIDINDO QUEM COMEÇA
        começa = randint(1,2)
        if começa % 2 == 0:
            compc = 1 #COMPUTADOR
        else: 
            compc = 2 #JOGADOR

        if compc == 1:
            escolhacomp = randint(1,2)
            if escolhacomp == 2:
                escolhacomp = 'par'
            else:
                escolhacomp = 'impar'
        #ESCOLHA COMP
        computador = randint(1,10)

        if compc == 1: #COMPUTADOR COMEÇA
            print(f'COMPUTADOR COMEÇA\nO computador escolheu {escolhacomp.upper()}')
            jogador = int(input('Informe que número vai jogar: '))
            system('cls')
            print(f'Você jogou {jogador} e o computador jogou {computador}!\nSomando dá {jogador+computador}')
            if ((escolhacomp == 'impar') and ((jogador+computador) % 2 != 0)) or ((escolhacomp == 'par') and ((jogador+computador) % 2 == 0)):
                print('Você perdeu!')
                vitoriacomp = 1
            else:
                print('Você Ganhou!')
                cont += 1
        else:
            print('O JOGADOR COMEÇA' )#JOGADOR COMEÇA
            parimpar = int(input('Par ou impar?\nNúmeros PARES = PAR\nNúmeros IMPARES = IMPAR\nFaça sua jogada: '))
            if parimpar % 2 == 0: parimpar = 'par'
            else: parimpar = 'impar'
            print(parimpar.upper(),'escolhido!!')
            jogador = int(input('Informe que número vai jogar: '))
            system('cls')
            print(f'Você jogou {jogador} e o computador jogou {computador}!\nSomando dá {jogador+computador}')
            if ((parimpar == 'impar') and ((jogador+computador) % 2 != 0)) or ((parimpar == 'par') and ((jogador+computador) % 2 == 0)):
                print('Você ganhou!')
                cont += 1
            else:
                print('Você perdeu')
                vitoriacomp = 1
        if vitoriacomp == 1:    
            print(f'Você ganhou {cont} vezes')
            break
    co = str(input('Deseja continuar?\n(SIM) - (NÃO)\n')).upper().strip().split()[0]
    system('cls')
print('Jogo encerrado')