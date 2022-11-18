nome=str(input('Informe o seu nome completo\n')).strip().title()
print('Olá',nome)
nomes=nome.split()
print('Seu primeiro nome é "{}" e seu ultimo nome é "{}"'.format(nomes[0],nomes[-1]))