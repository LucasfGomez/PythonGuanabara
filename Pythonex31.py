km = int(input('infome a distância da viagem\n'))
if km > 200:
    print('A viagem ultrapassou 200km, portanto, terá um desconto de 45 centavos por km')
    print('Você irá pagar R${} pela viagem'.format(km*0.45))
else:
    print('A viagem tem menos de 200km, portanto, será cobrado 50 centavos por km')
    print('Você irá pagar R${} pela viagem'.format(km*0.50))
