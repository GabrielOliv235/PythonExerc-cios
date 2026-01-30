num = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco')

while True:
    resp = int(input("Digite um numero de 0 à 5: "))
    if 0 <= resp <=5:
        print(num[resp])
        break
    else: print("Tente novamente")