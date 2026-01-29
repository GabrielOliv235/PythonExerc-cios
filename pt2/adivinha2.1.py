from random import randint

aleatorio = randint(0, 10)

while True:
    jogador = int(input("Chute um valor de 0 a 10: "))

    if jogador == aleatorio:
        print("Acertou!")
        break
    elif jogador > aleatorio:
        print("Menos")
    else:
        print("Mais")