# Exercicio 6: Faça um programa que crie uma lista vazia. Em seguida, o usuário deverá informar as notas de trabalhos obtidas (pode variar de 0 até quantos trabalhos forem informados). Por fim, mostre a média aritmética das notas obtidas.

trabalhos = []
nota_trabalho = 0
contador = 0

while True:
  trabalhos.append(float(input('Digite sua nota do trabalho: ')))

  r = str(input('Deseja continuar? (S - sim / N - não): '))
  if r in 'Nn':
    break

for indice, nota in enumerate(trabalhos):
  nota_trabalho = nota + nota + nota_trabalho  
  contador = contador + 1

nota_final = nota_trabalho / contador
print(f'Sua média aritmética é: {nota_final}')