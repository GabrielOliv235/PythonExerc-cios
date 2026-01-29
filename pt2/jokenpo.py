from random import randint

print('escolha : Pedra[0], Papel[1] ou Tesoura[2]')
jogador = int(input("Jogador1 :"))

itens = ('Pedra', 'Papel', 'Tesoura')

geraNumero = randint(0,2)
pc = geraNumero

print("Jogador1:",itens[jogador])
print("PC:",itens[pc])

if pc == 0:
    if jogador == 0:
        print("Empate")
    elif jogador == 1:
        print("Jogador  Ganhou")
    elif jogador == 2:
        print("PC ganhou")
    else:
        print("Invalido")
elif pc == 1:
    if jogador == 1:
        print("Empate")
    elif jogador == 0:
        print("PC Ganhou")
    elif jogador == 2:
        print("Jogador Ganhou")
    else:
        print("Invalido")
elif pc == 2:
    if jogador == 2:
        print("Empate")
    elif jogador == 0:
        print("Jogador Ganhou")
    elif jogador == 1:
        print("PC Ganhou")
    else:
        print("Invalido")











