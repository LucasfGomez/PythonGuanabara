from datetime import date
hoje = date.today().year
lista = ['primeira','segunda','terceira','quarta','quinta','sexta','setima']
cont=0
for c in range(0,7):
    ano = int(input('Digite o ano de nascimento da {} pessoa\n'.format(lista[c])))
    if (hoje - ano) > 21:
        cont+=1
print('{} pessoas são maiores de idade'.format(cont))
