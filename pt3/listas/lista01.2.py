num = [2,5,9,1]
print(num)
num[2] = 3
print(num)
num.append(7)
num.insert(2, 0)
print(num)
num.sort(reverse=True)
print(num)
num.pop(0)
print(num)
print(f'essa lista tem {len(num)} elementos')

if 9 in num:
    num.remove(9)
else:
    print("Não achei o valor")