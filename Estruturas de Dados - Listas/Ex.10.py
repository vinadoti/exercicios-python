# Exercicio 10: Faça um programa que contenha duas listas com 5 posições. Na primeira lista, deverá ser inserido o nome dos alunos. Na segunda lista, na mesma posição, a nota do aluno. Em seguida, mostre o nome dos alunos com a maior e a menor nota.

lista_alunos = []
lista_notas = []

while len(lista_alunos) < 3:
  nome = input('Insira o nome do aluno: ')
  lista_alunos.append(nome)
  nota = float(input('Insira a nota do aluno: '))
  lista_notas.append(nota)

maior = max(lista_notas)
maior_index = lista_notas.index(maior)
menor = min(lista_notas)
menor_index = lista_notas.index(menor)

print(lista_alunos, lista_notas)
print(f'A maior nota foi de {lista_alunos[maior_index]} - nota: {maior}')
print(f'A menor nota foi de {lista_alunos[menor_index]} - nota: {menor}')

# testes do código, ignore
# print(maior, menor, maior_index, menor_index)
# print(lista_alunos, lista_notas)
# # while len(lista_notas) < 5:
#   nota = float(input('Insira a nota do aluno'))