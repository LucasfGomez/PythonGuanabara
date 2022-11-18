from random import randint

comp = randint(1,3)
if comp == 1:
    comp1 ='Pedra'
elif comp == 2:
    comp1 ='Papel'
else:
    comp1='Tesoura'

print('Olá, vamos jogar?')
jog = int(input('''O que você quer escolher?
[1]Pedra
[2]Papel
[3]Tesoura\n'''))

if jog == 1:
    if comp1 == 'Pedra':
        print('Empate a máquina escolheu ',comp1)
    elif comp1 == 'Papel':
        print('Perdeu a máquina escolheu ',comp1)
    else:
        print('Ganhou a máquina escolheu ',comp1)

elif jog == 2:
        if comp1 == 'Pedra':
            print('Ganhou a máquina escolheu',comp1)
        elif comp1 == 'Papel':
            print('Empate a máquina escolheu',comp1)
        else:
            print('Perdeu a máquina escolheu ',comp1)

elif jog == 3:
        if comp1 == 'Pedra':
            print('Perdeu a máquina escolheu',comp1)
        elif comp1 == 'Papel':
            print('Ganhou a máquina escolheu',comp1)
        else:
            print('Empate a máquina escolheu',comp1)
else:
    print('Erro inesperado')
