#Exercicio 5: Faça um programa que carregue uma lista com dez números inteiros, informados pelo usuário. Em seguida, crie e mostre uma lista resultante ordenada de maneira crescente e crie e mostre uma lista resultante ordenada de maneira decrescente.

lista = []
lista_ordenada = []
lista_decrescente = []

while len(lista) < 10:
  numero = int(input('Insira um número inteiro: '))
  lista.append(numero)

lista_ordenada = sorted(lista)
lista_decrescente = sorted(lista, reverse = True)

print('Sua lista: ',lista)
print('Lista Ordenada: ',lista_ordenada)
print('Lista decrescente: ',lista_decrescente)