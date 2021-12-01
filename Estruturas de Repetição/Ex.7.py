# Exercício 7: Escreva um programa Python para construir o seguinte padrão, usando um número de loop aninhado. O usuário deverá informar um número.

numero=int(input('Digite um número: '))

for i in range(1, numero+1):
  print(str(i)*i)