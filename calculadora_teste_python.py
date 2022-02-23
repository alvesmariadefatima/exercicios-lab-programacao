alg1 = int(input('Digite o primeiro número: '))
alg2 = int(input('Digite outro valor: '))

resultado_soma = alg1 + alg2
resultado_subtracao = alg1 - alg2
resultado_multiplicacao = alg1*alg2
resultado_div = alg1/alg2
resto_divisao = alg1 % alg2

def soma (alg1, alg2):
    return alg1+alg2

print('-'*12)
print('{} + {} = {}'.format(alg1, alg2, resultado_soma))

def subtracao (alg1, alg2):
    return alg1-alg2
print('{} - {} = {}'.format(alg1, alg2, resultado_subtracao))

def multiplicacao (alg1, alg2):
    return alg1 * alg2
print('{} * {} = {}'.format(alg1, alg2, resultado_multiplicacao))

def div (alg1, alg2):
    return alg1/alg2
print('{} / {} = {}'.format(alg1, alg2, resultado_div))

def resto_div (alg1, alg2):
    return alg1 % alg2
print('{} % {} = {}'.format(alg1, alg2, resto_divisao))
print('-'*12)
