#Questão 2 - Fazer um programa que peça um valor na tela e mostrar se é positivo ou negativo

valor = int(input('Digite qualquer número: '))

if (valor >=0):
  print('{} é positivo.'.format(valor))

else:
    print('{} é negativo.'.format(valor))