frase = str(input('Digite uma frase\n')).lower().replace(' ','')
frasen = frase[::-1]
if frasen == frase:
    print('É um palindromo')
else:
    print('Não é um palindromo')