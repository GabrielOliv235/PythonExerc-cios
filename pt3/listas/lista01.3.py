valores = []
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor para a lista {cont}: ')))

for i, v in enumerate(valores) :
    print(f'Indice {i} valor {v}...')
print("Fim da lista")