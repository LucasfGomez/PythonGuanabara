'''um = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))

cont = 0
ultimo = um + (10-1) * razao

lista=[0,0,0,0,0,0,0,0,0,0]
while lista[9] != ultimo:
    ultimo = um + (10 - 1) * razao
    for c in range(um,(ultimo + razao),razao):
        lista[cont]= c
        cont += 1
print(lista)'''
####GUANABARA
total = 0
cont = 1
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} - ',end = '')
        termo += razao
        cont += 1
    print('pausa')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print('fim')
