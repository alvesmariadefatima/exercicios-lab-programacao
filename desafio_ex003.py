valor_compra_antes_aplicacao_promocao = float(input('Digite o valor da compra antes da aplicação da promoção: '))
valor_compra_depois_aplicacao_promocao = float(input('Digite o valor da compra depois da aplicação da promoção: '))
print('-'*12)
print('[0] - Pagamento a vista')
print('[1] - Pagamento a prazo')
opcao = str(input('Escolha a opção: '))
print('-'*12)
print('Valor da compra antes da aplicação: {:.2f}'.format(valor_compra_antes_aplicacao_promocao))
print('Valor aplicado de compra depois da promoção: {:.2f}'.format(valor_compra_depois_aplicacao_promocao))
print('Sua escolha da opção de pagamento é: {}'.format(opcao))


