frase=str(input('Digite uma frase:\n')).upper().strip()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {} e a ultima apareceu na posição {}'.format(frase.find('A')+1,frase.rfind('A')+1))
