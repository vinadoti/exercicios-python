#Exercicio 7: Implemente o jogo da forca. Um usuário deverá entrar com uma palavra. Em seguida, outro usuário deverá indicar as letras dessa palavra. Caso exista, deverá ser mostrada as letras e as suas posições na palavra. Caso não exista, o usuário perderá uma chance. No total, o usuário terá 6 chances para acertar.

# mostrando a lista de letras que o usuário escolheu e suas posições

palavra = input('Vamos lá! Pense em uma palavra: ').upper()
lista_forca = list(palavra)
lista_letras = []
contador = 0

while contador < 6:
  if lista_letras == lista_forca:
    print('\n Parabéns, você adivinhou a palavra!!')
    break
  letras = input('Pense em uma letra: ').upper()
  if letras in lista_forca:
    lista_letras.append(letras)
    print(f'{lista_letras} - Posição:{lista_forca.index(letras)}')
  else:
    print('Poxa, essa letra não constitui a palavra! Tentativas restantes:\
', 5 - contador,':(')
    contador+= 1 

print(f' A palavra era: {palavra} \n Suas tentativas foram: {lista_letras}')