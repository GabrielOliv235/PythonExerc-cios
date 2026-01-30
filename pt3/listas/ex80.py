lista = list()
for c in range(0, 5):
    num = int(input("Digite um numero: "))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Número adicionado com sucesso')
    else:
        pos = 0
        while pos <= len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print('Número adicionado com sucesso')
                break
            pos += 1
print(lista)