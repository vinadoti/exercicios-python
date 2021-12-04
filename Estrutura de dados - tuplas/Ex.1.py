# Faça um programa que carregue duas tuplas com nomes de alimentos, com 3 posições cada tupla. Em seguida, crie uma lista resultante da intercalação dessas duas tuplas. No final, mostre os itens dessa nova tupla.

alimentos1 = ('Chocolate', 'Bolacha', 'Ovos')
alimentos2 = ('Leite', 'Salgadinho', 'Arroz')

lista = [*sum(zip(alimentos1,alimentos2),())]

print(lista)