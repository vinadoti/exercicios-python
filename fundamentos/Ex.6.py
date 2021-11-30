#Exercício 6: Supondo que queremos pintar o muro da instituição, faça um programa que leia a altura e a largura do muro e mostre a quantidade de tinta necessária (1 litro de tinta pode pintar uma área de 2 metros quadrados).

altura = float(input('Digite a altura do muro:'))
largura = float(input('Digite a largura do muro:'))
area = (largura * altura) /2
print ("Quantidade de tinta necessária: {} ".format(area))