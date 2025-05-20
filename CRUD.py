usuarios = {}

contador_id = 1

def criar_usuario():
    global contador_id
    nome = input("Digite o nome do usuário: ")
    idade = int(input("Digite sua idade: "))
    usuarios[contador_id] = {"nome" : nome, "idade" : idade}
    print (f"Usuário: {nome}, idade: {idade}, com o id: {contador_id} Criado com sucesso!!")
    contador_id += 1

def listar_usuario():
    global usuarios
    if not usuarios:
        print("Nenhum usuário cadastrado")
    else:
        for id, usuario in usuarios.items():
            print(f"ID: {id}, Nome: {usuario['nome']}, Idade: {usuario['idade']}")

def buscar_usuario():
    global usuarios
    id = int(input("Digite o ID do usuário: "))
    if id in usuarios:
        usuario = usuarios [id]
        print(f"ID: {id}, Nome: {usuario['nome']}, Idade: {usuario['idade']}")
    else:
        print("Usuário não encontrado")

def atualizar_usuario():
    global usuarios
    id = int(input("Digite o ID de usuário que deseja atualizar: "))
    if id in usuarios:
        nome = input("Digite o novo nome de usuário: ")
        idade = int(input("Digite a nova idade: "))
        if nome:
            usuarios[id]["nome"] = nome
        if idade:
            usuarios[id]["idade"] = int(idade)
        print(f"Usuário {nome} atualizado com sucesso")
    else:
        print("Usuário não encontrado")

def deletar_usuario():
    global usuarios
    id= int(input("Digite o numero de ID que deseja excluir: "))
    if id in usuarios:
        del usuarios[id]
        print(f"Usuário {id} deletado")
    else:
        print("Usuário não encontrado")


def menu():
    while True:
        print("\n--- CRUD de Usuários ---")
        print("1. Criar usuário")
        print("2. Listar usuário")
        print("3. Buscar usuário por ID")
        print("4. Atualizar usuário")
        print("5. Deletar usuário")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_usuario()
        elif opcao == "2":
            listar_usuario()
        elif opcao == "3":
            buscar_usuario()
        elif opcao == "4":
            atualizar_usuario()
        elif opcao == "5":
            deletar_usuario()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    menu()
