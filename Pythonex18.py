import math
ang = float(input('Informe o angulo que você quer saber o Cosseno, Seno e Tangente\n'))
print('Segue o valor do Cosseno ({}), Seno({}) e Tangente({})'.format(math.cos(ang),math.sin(ang),math.tan(ang)))
#outra forma de se fazer
ang = float(input('informe o angulo que deseja\n'))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
sen = math.sin(math.radians(ang))
print('Segue o valor do Cosseno -={:.2f}=-, Tangente -={:.2f}=- e Seno -={:.2f}-=-'.format(cos,tan,sen))
