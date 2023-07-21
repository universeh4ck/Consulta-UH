print('\033[1m')
def js():
    print("error...")

print('\033[92m')
def UHV():
    print('\033[92m')
    print('\033[36m')
    print("==============================")
    print("****************************")
    print("CONSULTAS - by: universeh4ck")
    print("Servidor do discord: ")
    print("https://discord.gg/VFnTDshvXb")
    print("****************************")
    print("==============================")
    print("Consultas, cpf-telefone-gmail-nome")
    print("==============================")
    print("Para consultar nome: ")
    print("nome Vladimir Putin")
    print("==============================")
    print("Para consultar cpf: ")
    print("cpf 999.999.999-99")
    print("==============================")
    print("Para consultar telefone: ")
    print("telefone +55 21 99999-9999")
    print("==============================")
    print("Para consultar gmail:")
    print("gmail exemplo@gmail.com")
    print("==============================")
    bl = input('\033[93m Consulta:  \033[93m')
    if bl == "HPV":
        js()
    else:
        print("Consultando aguarde...")

    
def correct():
    universe = input("Você logou com sucesso. Deseja is para a ferramenta universeH? [S/N]")
    if universe == "S":
        UHV()
def incorrect():
    print("login or password incorrect")
login = input("Login: ")
if login == "UniverseH4ck":
    correct()
else:
    print("Login invalido.")