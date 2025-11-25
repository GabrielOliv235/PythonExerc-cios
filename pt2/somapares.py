soma = 0

for c in range (1,7):
    n = int(input(f"Valor N{c} :"))
    if n % 2 == 0:
        soma = soma + n

print("Total : ",soma)

