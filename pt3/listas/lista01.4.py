a =  list(range(10))
b = a #Ligação de uma lista e outra
b[2] = 8
print(f'lista original A : {a}')
print(f'lista B: {b}')

x = list(range(10))
y = x[:]##Cria uma copia
y[2] = 9
print(f'lista original X: {x}')
print(f'lista Y: {y}')