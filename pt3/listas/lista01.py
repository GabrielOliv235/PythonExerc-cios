num = [1,2,3,4,5,6]
print(num)
num[0] = 5 #Possivel
print(num)
num.append(7)
print(num)
num.sort(reverse=True)
print(num)
print(f'essa lista tem {len(num)} elementos')

num.insert(3,23)
print(num)
num.remove(23) #Remove elemento indicado
print(num)
num.pop(5) #Remove na posição indicada
print(num)
