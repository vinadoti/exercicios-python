# Faça um programa que leia quatro números pelo teclado e guarde-os em uma tupla. Em seguida, mostre:

# Quantas vezes apareceu o número 9.
# Em que posição foi digitado o primeiro valor 3.
# Quais foram os números pares.

print('Digite 4 números')
numeros = (int(input('1º número: ')), int(input('2º número: ')), int(input('3º número: ')), int(input('4º número: ')))

print(tuple(numeros))
print(f'O número 9 aparece {numeros.count(9)} vezes.')

if 3 in numeros:
    print(f'O número 3 foi digitado pela primeira vez na posição {numeros.index(3) +1}')
else:
    print('O número 3 não foi digitado')
print('Números pares digitados: ', end='')
for i in numeros:
    if i % 2 == 0:
        print(i, end=' ')