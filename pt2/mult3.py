for n in range(1,501, 2):
    print(n, end='. ')
    print(end="\n")
soma = 0
for c in range(1,501, 2):
    if c % 3 == 0:
        soma = soma + c

print("A soma dos multiplos é igual : {} ".format(soma))



