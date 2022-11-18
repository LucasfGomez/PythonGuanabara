vel=int(input('Qual é a velocidade atual do carro?\n'))
if vel<=80:
    print('Ok, continue assim')
else:
    print('Você foi multado!!!')
    print('Você deverá pagar uma multa de R$ {}!!!'.format((vel-80)*7))
#O de cima, eu fiz e o de baixo foi o professor Tanavara
