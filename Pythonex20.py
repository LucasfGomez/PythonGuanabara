import random
n1 = input('Informe o primeiro nome\n')
n2 = input('Informe o segundo nome\n')
n3 = input('Informe o terceiro nome\n')
n4 = input('Informe o quarto nome\n')
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('A ordem será',lista)