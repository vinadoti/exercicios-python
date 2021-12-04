#Exercicio 8:  Faça um programa em que o usuário deverá digitar os nomes de dez alunos da sala de aula. Em seguida, caso o programa encontre nomes repetidos, ele deverá alterar o nome adicionando o número sequencial. Por exemplo, se na lista tivermos dois "José", após o processamento a lista deverá conter "José 1" e "José 2".

lista = []
nomes = []
vezes = []
resultado = []

for i in range(0,3):
  lista.append(input(f'Digite o {i+1}º Nome:'))

for nome in lista:
  if nome not in nomes:
    nomes.append(nome)
    vezes.append(lista.count(nome))
    
for i, nome in enumerate(nomes):
  if vezes[i] == 1:
    resultado.append(nome)

  else:
    for j in range(0, vezes[i]):
      resultado.append(f'{nome} {j+1}') 

print(resultado)