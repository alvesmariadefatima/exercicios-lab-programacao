#Questão 14 - Fazer um programa que leia duas notas parciais de um aluno numa disciplina durante o semestre e calcular a média

nota1 = float(input('Digite a primeira nota do semestre: '))
nota2 = float(input('Digite a segunda nota do semestre: '))
media = (nota1 + nota2)/2

print('-'*12)
print('Nota 1: {}'.format(nota1))
print('Nota 2: {}'.format(nota2))
print('-'*12)
print('Sua média final é: {}'.format(media))
print('-'*12)
print('Média de aproveitamento - Conceito')
print('Entre 9.0 e 1.0 - Aprovado (A)')
print('Entre 7.5 e 9.0 - Aprovado (B)')
print('Entre 6.0 e 7.5 - Aprovado (C)')
print('Entre 4.0 e 6.0 - Reprovado (D)')
print('Entre 4.0 e zero - Reprovado (E)')
print('-'*12)
