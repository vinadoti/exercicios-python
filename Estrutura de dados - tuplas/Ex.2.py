# Faça um programa que carregue uma tupla com 5 números inteiros. Em seguida, crie e mostre uma tupla resultante ordenada de maneira crescente e crie e mostre uma tupla resultante ordenada de maneira decrescente.

# Da pra usar o random pra formar os números
#tupla_numeros = tuple(random.sample(range(0,10),5))

tupla_numeros = (1, 5, 2, 8, 12, 0)

tupla_crescente = sorted(tupla_numeros)
tupla_decrescente = sorted(tupla_numeros, reverse=True)

print(tuple(tupla_crescente))
print(tuple(tupla_decrescente))