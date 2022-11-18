print('Seja bem vindo à loja do Lucas')
preço = float(input('Preço das compras: R$'))
print('Você deseja fazer o pagamento de que forma?')
print('[1]À vista no dinheiro (10% de desconto)')
print('[2]À vista no cartão (5% de desconto')
print('[3]Em até 2x (Sem juros)')
print('[4]3x ou mais (10% de juros)')
pag = int(input('Sua opção: '))
if pag == 1:
    print('Em pagamentos à vista no dinheiro, o preço fica: R$', (preço - (preço * 0.1)))
elif pag == 2:
    print('Em pagamentos à vista no cartão, o preço fica: R$',(preço - (preço *0.05)))
elif pag == 3:
    print('Para pagamentos em 2x, a parcela: R$',preço/2)
elif pag == 4:
    vezes = int(input('Em quantas parcelas deseja pagar?\n'))
    total = (preço*1.2)
    parcela = (preço*1.2) / vezes
    print('Para pagamentos em {}x, o preço de cada parcela fica: R${} totalizando R$ {}'.format(vezes,parcela,total))
else:
    print('Opção invalida')
