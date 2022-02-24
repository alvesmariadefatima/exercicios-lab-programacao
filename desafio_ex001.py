#Preço Notebook -> R$ 1000,00 
#Preço Ipad -> R$ 1000,00

qtd_unidade_produto = int(input('Digite a quantidade de produtos comprados: '))
preco_total_comprado = float(input('Digite o preço da mercadoria: R$ '))
pgm_vista = preco_total_comprado - (preco_total_comprado*10/100)
pgm_prazo = preco_total_comprado + (preco_total_comprado*8/100) 

print('-'*12) 
print('Valor com desconto pagando a vista: R$ {:.2f}'.format(pgm_vista))
print('Valor com acréscimo pagando a prazo: R$ {:.2f}'.format(pgm_prazo))
print('-'*12)
    
