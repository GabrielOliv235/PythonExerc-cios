valorDaCasa = int(input('Valor da casa: '))
valorSalario = int(input('Seu salario: '))
anosPagar = int(input('Anos para pagar: '))

saldoEmprest = valorSalario/100 * 30

parcela = valorDaCasa/(anosPagar*12)
print(f"Valor da parcela : {parcela}")

if parcela <= saldoEmprest:
    print("Emprestimo aprovado")
else:
    print("Emprestimo não aprovado")



##Naõ pode excerder 30% do salario