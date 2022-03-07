#Questão 8 - Fazer um programa que leia 5 números e faça a média aritmética entre esses valores

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
n4 = float(input('Nota 4: '))
n5 = float(input('Nota 5: '))

soma = n1 + n2 + n3 + n4 + n5
media_geral = (n1+n2+n3+n4+n5)/5

print('A soma total é: {}'.format(soma))
print('A média geral desses 5 números é: {}'.format(media_geral))