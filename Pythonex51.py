print('Verificar termos de uma PA(Progressão Aritmética')
um = int(input('Informe o primeiro termos da PA\n'))
razao = int(input('Informe a razão da PA\n'))
ultimo = um + (10 - 1) * razao
for c in range(um,(ultimo + razao),razao):
    print(c,'- ',end='')
print('FIM')