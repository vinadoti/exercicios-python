#Exercício 3: Implemente um programa que leia 4 notas de um aluno e mostre a média aritmética.

nota1,nota2,nota3,nota4 = input("Digite as suas notas ").split()
media = (float(nota1) + float(nota2) + float(nota3) + float(nota4) ) /4
print("Média final = ", media)