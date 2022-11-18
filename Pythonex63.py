#Sequencia fibonacci
from os import system
n = int(input('Quantos números da sequencia Fibonacci você quer ver?'))
c = 0
b = 1
a = 0
cont = 0
system('cls')
for cont in range(0,n):
    print(c,end='-')
    c = a + b
    b = a
    a = c
print('Final')
