# Exercício 6: Você recebe uma string e uma largura. Sua tarefa é envolver a string em um parágrafo com esta largura (text wrapper).
# Input: "Texto muito longo", largura:

#OutPut: Text

#o mu

#ito

#long

#o

texto= input("insira um texto: ")
largura = int(input("insira a largura: "))
var_controle = largura
for i in range(0,len(texto)):
  print(texto[i], end= '')
  if i == (largura - 1):
    print("\n")
    largura = largura + var_controle