print("**Programa Iniciado**")
opcoes = 1,2,3
menu = int(input("""MENU - OPÇÕES
    1 ) LOGIN
    2 ) CADASTRAR
    3 ) SAIR
    : """))

while menu not in opcoes:
    menu = int(input("""MENU - OPÇÕES
    1 ) LOGIN
    2 ) CADASTRAR
    3 ) SAIR
    : """))

print("Fim do Programa")