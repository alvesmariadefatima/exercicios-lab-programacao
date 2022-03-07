#Questão 1 - Fazer um programa que peça uma nota entre zero e dez

nota=float(input("informe um numero de 0 a 10: "))
while (nota>10) or (nota<0):
	nota=float(input("informe um numero de 0 a 10: "))