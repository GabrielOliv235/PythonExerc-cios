from random import randint
aleatorio = randint(0,10)
acerto = False
while not acerto:
    jogador = int(input("Chute um valor de 0 a 10 : "))
    if jogador == aleatorio:
        acerto = True
    elif jogador > aleatorio:
        print("Menos")
    elif jogador < aleatorio:
        print("Mais")
print("Acertou")