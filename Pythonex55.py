lista = ['primeira','segunda','terceira','quarta','quinta']
maior = 0
menor = 0
for c in range(0,5):
    peso = float(input(f'Informe o peso da {lista[c]} pessoa\n'))
    if c == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'O maior peso é {maior} e o menor é {menor}')
