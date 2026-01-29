print("**Programa Iniciado**")

while True:
    menu = int(input("""MENU - OPÇÕES
    1 ) LOGIN
    2 ) CADASTRAR
    3 ) SAIR
    : """))

    if menu == 1:
        print("Você escolheu LOGIN")

    elif menu == 2:
        print("Você escolheu CADASTRAR")

    elif menu == 3:
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida! Tente novamente.")
