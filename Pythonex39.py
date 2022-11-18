from datetime import date

nasc = int(input('Em que ano você nasceu?\n'))
ano = date.today().year
idade = (ano - nasc)
print('Você possui {} anos de idade!'.format(idade))
if idade > 18:
    print('Seu alistamento foi à {} anos atrás, você se alistou?'.format(idade-18))
elif idade < 18:
    print('Seu alistamento será daqui {} ano(s), se prepare para o alistamento'.format(18-idade))
else:
    print('Portanto deverá se alistar IMEDIATAMENTE')
