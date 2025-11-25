##Faça um programa que leia um ângulo qualquer e mostre na tela o valor
##do seno, cosseno e tangente desse ângulo.
import math
ang = float(input("Digite o ângulo desejado :"))
print('Angulo {} tem o seno de {:.2f}'.format(ang, math.sin(math.radians(ang))))
print('Angulo {} tem o cosseno de {:.2f}'.format(ang, math.cos(math.radians(ang))))
print('Angulo {} tem o tangente de {:.2f}'.format(ang, math.tan(math.radians(ang))))