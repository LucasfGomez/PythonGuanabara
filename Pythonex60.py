fat = int(input('Informe o número que você quer fatoriar ?\n'))
n = fat
f = 1
while n > 0:
    print(n,end = ' ')
    print('x',end = ' ') if n > 1 else print('=',end = ' ')
    f *= n
    n -= 1
print(f)