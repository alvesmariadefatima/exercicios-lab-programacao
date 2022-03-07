#Questão 10 - Fazer um programa para perguntar ao usuário em qual turno estuda

matutino = 'M'
vespertino = 'V'
noturno = 'N'

print('-'*12)
print('M - Matutino')
print('V - Vespertino')
print('N - Noturno')
print('-'*12)
opcao = str(input('Escolha qual turno você estuda: '))

if (opcao ==  matutino):
  print('Bom dia!')

if (opcao == vespertino):
         print('Boa tarde!')

if (opcao == noturno):
      print('Boa noite!')