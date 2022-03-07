#Questão 7 - Calcular a área do quadrado e mostrar o dobro do resultado digitado pelo usuário

l1 = int(input('Digite um valor para o lado do quadrado: '))
l2 = int(input('Digite outro valor para o lado do quadrado: '))

area = 2*(l1*l2)

print('Lado 1 = {}'.format(l1))
print('Lado 2 = {}'.format(l2))
print('O dobro desta área corresponde a {}'.format(area))