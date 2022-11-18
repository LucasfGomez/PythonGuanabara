nmr = int(input('Escolha um número\n'))
nmrpi = nmr % 2
if nmrpi == 0:
    print('O número {} é par!'.format(nmr))
else:
    print('O número {} é impar!'.format(nmr))
