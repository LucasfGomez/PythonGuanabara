lar=float(input('Informe a largura da parede\n'))
alt=float(input('Informe a altura da parede\n'))
area=lar*alt
litro=area/2
print('Se com 1 litro você pode pintar 2m², você precisará de {} Litros de tinta, já que a parede possui {}m²'.format(litro,area))