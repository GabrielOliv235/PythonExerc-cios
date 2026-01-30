print('INICIO')
lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor {c} : ')))
mai = max(lista)
men = min(lista)
print(f'Lista: {lista}')
print(f'Maior valor: {mai}, nas posições:', end=' ')
for indice , valor in enumerate(lista):
    if valor == mai:
        print(indice, end=' ')
print(f'\nMenor valor: {men}, nas posições:', end=' ')
for indice, valor in enumerate(lista):
    if valor == men:
        print(indice, end=' ')

