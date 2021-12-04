# Exercicio 3: Faça um programa que carregue duas listas com nomes de animais, com 5 posições cada lista. Em seguida, crie uma lista resultante da intercalação dessas duas listas. No final, mostre os itens dessa nova lista.

lista1 = ['Ovelha', 'Vaca', 'Camaleão', 'Cachorro', 'Avestruz']
lista2 = ['Gato', 'Lagarto', 'Hamster', 'Rato', 'Coelho']
intercalar = []

for i in range(5):
  intercalar.append(lista1[i])
  intercalar.append(lista2[i])

print(intercalar)