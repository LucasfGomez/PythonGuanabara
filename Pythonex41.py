from datetime import date 
nasc = int(input('Qual seu ano de nascimento?\n'))
hoje = date.today().year
idade = hoje-nasc

if idade <= 9:
    print('Mirim, sua idade é {}'.format(idade))
elif 9 < idade <= 14:
    print('Infaltil, sua idade é {}'.format(idade))
elif 14 < idade <= 19:
    print('Junior, sua idade é {}'.format(idade))
elif 19 < idade <= 25:
    print('Senior, sua idade é {}'.format(idade))
else:
    print('MASTER, sua idade é {}'.format(idade))