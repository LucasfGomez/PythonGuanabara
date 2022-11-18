from os import system
print('-'*10,'TABUADA','-'*10,'\n')
tab = int(input('Informe o número que você quer ver a tabuada: '))
while True:
        if tab < 0:
            system('cls')
            break
        else:
            for c in range(0,11):
                    print(f'{tab} x {c} = {tab*c}')
            tab = int(input('Deseja continuar?\nSe sim, digite um novo valor: '))
        system('cls')
print('Calculadora finalizada, espero ter ajudado em suas contas!\n')
