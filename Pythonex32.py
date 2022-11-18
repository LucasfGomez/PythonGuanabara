import datetime
ano=int(input('Informe o ano que você quer saber se é BISSEXTO ou não\nInforme 0 para analisar o ano atual\n'))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))