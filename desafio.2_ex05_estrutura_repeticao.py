#Questão 48 - Fazer um programa para que o usuário digite um valor e no final inverter a sequência dos algoritmos

num=int(input('Digite qualquer valor: '))
if num > 0:
    a = num%100
    b = num//100%100
    d = str("%d%d"%(a, b))
    print(d)
else:
    num_ajus = num_ajus *100 + d
    print(num_ajus)
