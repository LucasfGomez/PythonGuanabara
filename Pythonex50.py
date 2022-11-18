total = 0
lista = ['primeiro','segundo','terceiro','quarto','quinto','sexto']
for c in range(0,6):
    n = int(input('Digite o {} que quer adicionar à somatória\n'.format(lista[c])))
    if n % 2 == 0:
        total += n
print(total)
