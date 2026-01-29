num = (1,2,3,4,5,6,7,8,9,10)
while True:
    resp = int(input("Digite um número de 1 e 5:"))
    if resp in num:
        if resp == 1:
            print("um")
            break
        elif resp == 2:
            print("Dois")
            break
        elif resp == 3:
            print("Tres")
            break
        elif resp == 4:
            print("Quatro")
            break
        elif resp == 5:
            print("cinco")
            break
        else:
            print("Número invalido")
            break

    else:
        print("Número invalido")
        break