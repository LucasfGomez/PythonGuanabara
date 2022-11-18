npode='''=================================================================
= O triangulo não pode ser formado com as informações passadas. =
================================================================='''

pode=0
linha1 = float(input('Informe o tamanho da primeira reta: '))
linha2 = float(input('Informe o tamanho da segunda reta: '))
linha3 = float(input('Informe o tamanho da terceira reta: '))
if linha1 < linha2 + linha3 and linha2 < linha1 + linha3 and linha3 < linha1 + linha2:
    pode=1
    print('============================\n| Pode formar um triangulo |\n============================')     
else:
    pode=2
    print(npode)

if pode==1:
    if(linha1 == linha2 and linha2 == linha3) and (linha2 == linha3 and linha3 == linha1) and (linha3 == linha1 and linha1 == linha2):
        print('É um triangulo Equilatero') 
    elif (linha1 != linha2 and linha2 != linha3) and (linha2 != linha3 and linha3 != linha1) and (linha3 != linha1 and linha1 != linha2):
            print('É um triangulo Escaleno')
    else:
        print('É um triangulo Isóceles')
 