# Faça um programa que contenha uma tupla com diversas palavras. Para cada palavra, mostre suas vogais no seguinte formato: 'A palavra Fatec contém as vogais a e'.

tupla_palavras = ('Fatec', 'escola', 'livros', 'caderno', 'lousa')

for palavra in tupla_palavras:
    print(f'A palavra {palavra.upper()} contém as vogais: ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    print('\n')