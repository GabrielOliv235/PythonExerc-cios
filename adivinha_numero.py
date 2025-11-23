import random
adivinha = int(input('Digite um número de 1 - 5 :'))
nrandom = random.randint(1, 5)

if adivinha == nrandom :
    print('Você acertou :{} '.format(nrandom))
else:
    print('Você errou o número correto era :{}'.format(nrandom))
