# Exercício 4: Implemente um programa que leia um valor em metros e mostre seu valor em centímetros e em milímetros.

m = float(input("Digite uma distância em metros: "))
cm = m * 100
mm = m * 1000
print("{}m corresponde a {}cm e {}mm".format(m, cm, mm))