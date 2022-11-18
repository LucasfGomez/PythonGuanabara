lista = ['primeira','segunda','terceira','quarta','quinta']
totali = 0
maior = 0
cont = 0
nomev = ''
for c in range(0,4):
    nome = str(input(f'Qual o nome da {lista[c]} pessoa?\n'))
    idade = int(input(f'Qual a idade da {lista[c]} pessoa?\n'))
    sexo = str(input(f'Qual o sexo da {lista[c]} pessoa? [M] / [F]\n')).upper()
    print('='*20)
    totali += idade
    if sexo == 'M' and idade > maior:
        maior = idade
        nomev = nome
    elif sexo == 'F' and idade < 20:
        cont += 1
print(f'A media de idade é {totali/4}')
print(f'O homem mais velho é o {nomev.title()} que possui {maior} anos')
print(f'{cont} mulheres têm menos de 20 anos')