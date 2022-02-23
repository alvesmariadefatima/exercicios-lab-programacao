#Desafio 02 - Laços de repetição

a, b = input().split()
a, b = int(a), int(b)
media = (a+b)/2
print(media)

a, b = input().split()
a, b = int(a),int(b)
media = (a+b)/2
print(media)

a, b = input().split()
a, b = int(a), int(b)
media = (a+b)/2
print(media)


for i in range(3):
  a, b = input().split()
  a, b = int(a), int(b)
  media = (a+b)/2
  print(media)
  print("LOOP", i)
   
5 == (3+2)

5 == 6

j = "hel"
j + "lo" == "hello"

int(1) != "Hello"

j = "hel"
j + "lo" == "hello"

int(1) != "Hello"

#Lógica usando tabela verdade

#x and False == False
#False and x == False

c = True
c and b != b and c

#x and True == x
#True and x == x
#x and x == x

#Estrutura de decisão if else

x = float(input('Digite qualquer valor: '))

if x%2 ==0:
  print(x, "é par.")
  print("Você sabia que o 2 é o único número par que é primo? ")
else:
    print(x, "é ímpar.")
    print("Você sabia que a multiplicação de dois números ímpares" + "sempre resulta em um número ímpar?")
