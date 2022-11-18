sal=float(input('Informe o valor do seu salário: '))
if sal < 1250:
    nsal = sal * 1.15
    print('Como seu salário é uma mizéria, aumentamos 15%\nAgora você recebe: R$',nsal)
else:
    nsal = sal * 1.1
    print('Já que você já recebe bastante, aumentamos apenas 10%\nAgora você recebe: R$',nsal)
