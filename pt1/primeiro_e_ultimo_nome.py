n = str(input('Digite seu nome: ')).strip()
nome = n.split()
print('seu primeiro nome é : {}'.format(nome[0]))
print('seu último nome é : {}'.format(nome[len(nome)-1]))

