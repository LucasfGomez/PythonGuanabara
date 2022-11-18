nome=input('Digite seu nome completo\n')
print('Seu nome todo maiusculo é: {}'.format(nome.upper()))
print('Seu nome todo minusculo é: {}'.format(nome.lower()))
print('Seu nome sem espaços é: {} e possui {} letras(desconsiderando espaços)'.format(nome.replace(' ',''),len(nome.replace(' ',''))))
dividido=nome.split()
print('Seu primeiro nome possui {} letras'.format(len(dividido[0])))
#Os de cima eu fiz, o de baixo foi o Guanabara.
'''nome=str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letas'.format(nome.find(' ')))'''