import os
print('Sejá bem vindo ao simulador de emprestimo')
vcasa=float(input('Qual é o valor da casa que você quer comprar?\n'))
sal=float(input('Qual é o seu salário?\n'))
tem=int(input('Em quantos meses você deseja pagar a casa?\n'))

os.system('cls')
ent=str(input('Você deseja dar um entrada?(Sim/Não)\n')).upper().strip()

valpar=(vcasa/tem)
if ent == 'NÃO' or ent == 'N' or ent == 'NAO' or ent == 'NA' or ent == 'NO':
    if valpar >= (sal * 0.3):
     print('Financiamento negado, o valor da parcela é superior a 30% do seu salário\n{}'.format(valpar))
    else:
        print('FINANCIAMENTO APROVADO\nA parcela será de R${:.2f}'.format(valpar))

elif ent == 'SIM' or ent == 'SI' or ent == 'S' or ent == 'IM':
    vent=(float(input('De quanto será a entrada?')))
    valpar=((vcasa-vent)/tem)
    if valpar >= (sal * 0.3):
        print('Financiamento negado, o valor da parcela é superior a 30% do seu salário\n{:.2f}'.format(valpar))
    else:
        print('FINANCIAMENTO APROVADO\nA parcela será de R${:.2f}'.format(valpar))
