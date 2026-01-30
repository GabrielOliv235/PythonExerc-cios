lista = list()
while True:
    n = (int(input('Digite um valor: ')))
    if n in lista:
        print("Valor já existe! Valor não adicionado")
        len(lista)
        delet = max(lista)
        lista.remove(delet)
    lista.append(n)
    cont = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if cont == 'N':
        print('Encerrando...')
        break
    elif cont == 'S':
        print(end='')
    else:
        print("erro!!! *comando invalido*")
        break
print(f"Numeros digitados: {lista.sort(reverse=True)}")