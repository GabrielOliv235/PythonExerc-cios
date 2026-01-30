lista = list()
while True:
    lista.append(int(input('Digite um valor para ser adicionado: ')))
    print('Número adicionado')
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'Nn':
        break
print(lista)
print(len(lista))
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('Valor 5 apareceu na lista')
else:
    print('Valor 5 not in lista')


