totalpreço = maismil = cont = 0
nomebarato = nome = str(input('Informe o nome do produto: '))
barato = preço = float(input('Informe o preço do produto: R$'))
while True:
    totalpreço += preço
    if preço > 1000:
        maismil += 1
    if cont > 0 and preço < barato:
        barato = preço
        nomebarato = nome
    cont += 1
    conti = str(input('Deseja continuar? [S-N]: ')).upper().strip()[0]
    if conti == 'N':
        break
    nome = str(input('Informe o nome do produto: '))
    preço = float(input('Informe o preço do produto: R$'))
print(f'Cadastramos {cont} produtos!')
print(f'O total da conta foi R${totalpreço}')
print(f'Tivemos {maismil} produtos custando mais que R$1000')
print(f'O produto mais barato foi a {nomebarato} que custou R${barato}')