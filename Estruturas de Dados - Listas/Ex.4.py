#Faça um programa que crie duas listas x e y, com dez números inteiros cada uma. Os valores deverão ser informados pelo usuário e os valores não podem se repetir dentro de uma lista. Em seguida, crie:

# Uma lista resultante da união de x e y (todos os elementos de x e os elementos de y que não estão em x).

# Uma lista resultante da diferença entre x e y (todos os elementos de x que não existam em y).

# Uma lista resultante da some de x e y (soma de cada elemento de x com o elemento de y na mesma posição)

lista = []
lista2 = []
lista_diferenca = []
lista_soma = []
 
while len(lista) < 5: #for numero in range(10)
  numero = int(input('Insira um número inteiro para a primeira lista: '))
  if numero not in lista:
    lista.append(numero)
  else:
    print('Você já inseriu esse número, tente outro: ')
while len(lista2) < 5:
  numero = int(input('Insira um número inteiro para a segunda lista: '))
  if numero not in lista2:
    lista2.append(numero)
  else:
    print('Você já inseriu esse número, tente outro: ')
 
lista_uniao = list(lista)
for uniao in lista2:
  if uniao not in lista:
    lista_uniao.append(uniao)

for diferente in lista:
  if diferente not in lista2:
    lista_diferenca.append(diferente)

for soma in range(len(lista)): # soma representa o tamanho da lista(10)
  lista_soma.append(lista[soma]+lista2[soma]) # soma de cada elemento 
                                              # correspondente a seu índice
print('Lista x:',lista)
print('Lista y:',lista2)
print('União da listas:',lista_uniao)
print('Diferença das listas:',lista_diferenca)
print('Soma das listas:',lista_soma)
