sex = str(input('Informe seu sexo(M/F)\n')).upper().strip()[0]
while (sex != 'F' and sex != 'M'):
    print(f'Você digitou erroneamente, {sex} não é o que foi pedido!\n')
    sex = str(input('Informe seu sexo(M/F)\n')).upper().strip()[0]
if sex == 'M':
    sex = 'cabra macho'
else:
    sex = 'princesa do norte'
print(f'Ok, você é do sexo {sex}')