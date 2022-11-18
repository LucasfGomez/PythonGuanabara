from os import system
from time import sleep
nmr = int(input('Informe o número que você quer converter:\n'))
con = int(input('Você quer converter o número {} para qual sistema?\n[1] - Binário\n[2] - Octal\n[3] - Hexadecimal\n'.format(nmr)))
system('cls')
if con == 1:
    print('(Binário) Selecionado\nO número {} convertido para Binário é: {}'.format((nmr),bin(nmr)[2:]))
elif con == 2:
    print('(Octal) Selecionado\nO número {} convertido para Octal é: {}'.format((nmr),oct(nmr)[2:].upper()))
elif con == 3:
    print('(Hexadecimal) Selecionado\nO número {} convertido para Hexadecimal é: {}'.format((nmr),hex(nmr)[2:].upper()))
else:
    print('Opção invalida\n ----ERROR----')
