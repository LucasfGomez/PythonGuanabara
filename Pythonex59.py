from time import sleep
from os import system
esc = 4

while esc == 4:
    print('Seja bem vindo à calculadora do Luquinhas')
    print("""Que tipo de conta você deseja fazer?
[1]Soma
[2]Multiplicação
[3]x maior que y
[4]Novos números
[5]Sair""")
    esc = int(input('Faça sua escolha: '))
    if esc == 1:
        n = float(input('Digite o primeiro número da soma: '))
        n2 = float(input('Digite o segundo número da soma: '))
        print(f'{n} + {n2} = {n+n2}')
    elif esc == 2:
        n = float(input('Digite o primeiro número da multiplicação: '))
        n2 = float(input('Digite o primeiro número da multiplicação: '))
        print(f'{n} x {n2} = {n*n2}')
    elif esc == 3:
        n = float(input('Digite o primeiro número que quer verificar: '))
        n2 = float(input('Digite o primeiro número que quer verificar: '))
        if n > n2:
            print(f'{n} é maior que {n2}')
        else:
            print(f'{n2} é maior que {n}')
    elif esc == 4:
        print('Reiniciando calculadora')
        for c in range(0,10):
            sleep(0.5)
            print()
        system('cls')
        esc = 4
    elif esc == 5:
        system('cls')
        print('Ok, tenha um ótimo dia!!')
        sleep(1)
        print('=D')
    else:
        print('Número não esperado, calculadora encerrada.')
        print('Você me bugoououooouooou')
        sleep(0.7)
        for c in range(1,10):
            if c % 2 == 0:
                sleep(0.4)
                print('Autodestruição')
            else:
                sleep(0.7)
                print('O que está acontecendo?')
        print('BUUUUUM!!!!')
        sleep(1)
        system('cls')
        for c in range(1,10):
            if c % 2 == 0:
                sleep(1)
                system('cls')
                print('Calculadora encerrada..')
            else:
                sleep(1)
                system('cls')
                print('Calculadora encerrada...')

