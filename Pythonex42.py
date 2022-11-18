
linha1 = float(input('Informe o tamanho da primeira reta: '))
linha2 = float(input('Informe o tamanho da segunda reta: '))
linha3 = float(input('Informe o tamanho da terceira reta: '))
npode='''=================================================================\n= O triangulo não pode ser formado com as informações passadas. =\n================================================================='''
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

#O meu código é o de cima, o de baixo é o do Guanabara, para comentar use (""")

r1 = float(input('Primeiro segmento\n'))
r2 = float(input('Segundo segmento\n'))
r3 = float(input('Terceiro segmento\n'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triangulo ',end='')
    if r1 == r2 == r3:
        print('Equilatero')
    elif r1 != r2 != r3 != r1:
        print('Escaleno')
    else:
        print('Isoceles')
else:
    print('Não pode formar um triangulo')
