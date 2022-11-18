from time import sleep
from os import system
system('cls')
print('Seja bem vindo a calculadora de IMC')
sleep(2)
print('.')
system('cls')
print('..')
sleep(0.5)
system('cls')
print('...')
sleep(0.5)
system('cls')
print('Para fazer o calculo, preciso de algumas informações suas')
peso = float(input('Informe seu peso\n'))
altu = int(input('Informe usa altura\n'))
imc = (peso / ((altu/100)**2))

if imc > 40:
    print('Obesidade morbida(famoso gordalhão)',imc)
elif 40 > imc > 30:
    print('Obesidade(Gordão)',imc)
elif 30 > imc > 25:
    print('Sobrepeso(Gordin)',imc)
elif 25 > imc > 18.5:
    print('Peso ideal(Mas se cuida em)',imc)
else:
    print('Abaixo do peso(Vara pau)',imc)
