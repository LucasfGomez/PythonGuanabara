import math

#calculo sem math
cto=float(input('Informe o tamanho do Cateto Oposto\n'))
cta=float(input('Informe o tamanho do Cateto Adjacente\n'))

hip = ((cta*cta) + (cto * cto)) ** (1/2)
print('O valor da hipotenusa é: {:.2f}'.format(hip))
#calculo com math
cto=float(input('Informe o valor do Cateto Oposto\n'))
cta=float(input('Informe o valor do Cateto Adjacente\n'))
hi=math.hypot(cto,cta)
print('O valor da hiportenusa é: {}'.format(hip))