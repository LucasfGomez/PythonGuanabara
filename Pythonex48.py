total=0
cont=0
for c in range(1,501):
    if c % 3==0 and c % 2 != 0:
        cont += 1
        print(c)
        total += c
print(total)
print(cont)
