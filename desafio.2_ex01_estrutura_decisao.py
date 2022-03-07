#Questão 5 - Fazer um programa para a leitura de duas notas parciais do aluno e verificar seu status de aprovação

n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))

media = (n1+n2)/2

if (media >= 7):
  print('Aprovado')

  if(media < 7):
    print('Reprovado')
       
  if (media == 10):
        print('Aprovado com Distinção')
