print('Calculo de média')
n1=float(input('Informe a primeira nota do aluno\n'))
n2=float(input('Informe a segunda nota do aluno\n'))
n3=float(input('Informe a terceira nota do aluno\n'))

m=(n1+n2+n3)/3

if 5 <= m < 7:
    print('Sua nota é: {:.1f}\nVocê está de recuperação'.format(m))
elif m >= 7:
    print('Sua nota é: {:.1f}\nVocê está aprovado'.format(m))
else:
    print('Sua nota é: {:.1f}\nVocê está reprovado'.format(m))
