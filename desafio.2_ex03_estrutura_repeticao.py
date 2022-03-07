#Questão 18 - Fazer um programa que peça uma data no formado dd/mm/aaaa

dia = int(input('Digite o dia que você nasceu: '))
mes = int(input('Digite o mês que você nasceu: '))
ano = int(input('Digite o ano que você nasceu: '))

print('{} / {} / {}'.format(dia, mes, ano))

data_valida = str(input('Esta data é válida? '))

print('{}/{}/{} é uma data válida.'.format(dia, mes, ano))

