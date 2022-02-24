from unittest import FunctionTestCase


qtd_notebooks = int(input('Digite a quantidade de notebooks que deseja comprar: '))
qtd_ipads = int(input('Digite a quantidade de ipads que deseja comprar: '))
print('-'*12)
print('Quantidade de notebooks: {} '.format(qtd_notebooks))
print('Quantidade de ipads: {} '.format(qtd_ipads))
print('-'*12)
print('Escolha a opção abaixo: : ')
print('[0] - Pagamento a vista')
print('[1] - Pagamento a prazo')
opcao = str(input('Escolha sua opção: '))
print('Você escolheu a opção {}'.format(opcao))


