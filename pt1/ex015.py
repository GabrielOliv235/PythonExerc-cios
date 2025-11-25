import math
num1 = float(input('Digite o valor do cateto oposto:'))
num2 = float(input('Digite o valor do cateto adjacente:'))
print('O valor do catedo oposto é {}, o valor do cateto adjacente é {} logo o valor da hipotenusa é {:.2f}'.format(num1, num2, math.hypot(num1, num2)))