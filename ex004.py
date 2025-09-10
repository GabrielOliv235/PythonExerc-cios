from curses.ascii import isalnum

n1 = input('Digite algo: ')
print('O que você digitou || {0} ||'.format(n1))
print('O tipo primitivo desse valor é', type(n1))
print('Só tem espaço?', n1.isspace())
print('É um numero?', n1.isnumeric())
print('É alfabetico?', n1.isalpha())
print('É alpha númerico?', n1.isalnum())
print('Está em minúscula?', n1.islower())
print('Está me maiúscula?', n1.isupper())
