p18=h=m20=cad=0
cont = ''
while True:
    idade = int(input('Informe a idade que quer cadastrar: '))
    sexo = str(input('Informe o sexo que quer cadastrar[M-F]: ')).upper().strip()[0]
    if idade > 18:
        p18+=1
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo que quer cadastrar[M-F]: ')).upper().strip()[0]
    if sexo == 'M':
        h+=1
    if idade < 20 and sexo == 'F':
        m20 += 1
    cad+=1
    cont = str(input('Deseja continuar? [S-N]: ')).upper().strip()[0]
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S-N]: ')).upper().strip()[0]
    if cont == 'N':
        break
print(f'Foram cadastradas {cad} pessoas!\n{p18} tem mais de 18 anos!')
print(f'{h} homens foram cadastrados!\n{m20} mulheres têm menos de 20 anos!')
