nome = str(input("qual é seu nome : "))
if nome == "gabriel":
    print('nome legal')
elif nome == "paula" or nome == "pedro" or nome == "vitor" :
    print('belo nome')
elif nome in "Ana claudia jessica juliana":
    print("Nome feminino")

else:
    print("Bom dia")