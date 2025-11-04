# === SISTEMA CLÍNICA VIDA+ ===
# Desenvolvido por: Alexandra Cordeiro
# Objetivo: Cadastrar pacientes, exibir estatísticas e permitir buscas.

# Lista principal para armazenar pacientes
pacientes = []

# Função para cadastrar paciente
def cadastrar_paciente():
    print("\n=== CADASTRAR PACIENTE ===")
    try:
        nome = input("Nome do paciente: ").strip().title()
        idade = int(input("Idade: "))
        telefone = input("Telefone: ").strip()

        # Cria um dicionário com os dados
        paciente = {
            "nome": nome,
            "idade": idade,
            "telefone": telefone
        }

        pacientes.append(paciente)
        print(f"✅ Paciente {nome} cadastrado com sucesso!")
    except ValueError:
        print("⚠️ Erro: idade deve ser um número inteiro.")

# Função para exibir estatísticas
def ver_estatisticas():
    print("\n=== ESTATÍSTICAS ===")
    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado.")
        return

    total = len(pacientes)
    idades = [p["idade"] for p in pacientes]
    media = sum(idades) / total
    mais_novo = min(pacientes, key=lambda p: p["idade"])
    mais_velho = max(pacientes, key=lambda p: p["idade"])

    print(f"📋 Total de pacientes: {total}")
    print(f"📊 Idade média: {int(round(media))} anos")
    print(f"🧒 Paciente mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
    print(f"👴 Paciente mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)")

# Função para buscar paciente pelo nome
def buscar_paciente():
    print("\n=== BUSCAR PACIENTE ===")
    nome_busca = input("Digite o nome do paciente: ").strip().title()
    encontrados = [p for p in pacientes if nome_busca in p["nome"]]

    if encontrados:
        for p in encontrados:
            print(f"👤 Nome: {p['nome']} | Idade: {p['idade']} | Telefone: {p['telefone']}")
    else:
        print("❌ Paciente não encontrado.")

# Função para listar todos os pacientes
def listar_pacientes():
    print("\n=== LISTA DE PACIENTES ===")
    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado.")
        return

    for i, p in enumerate(pacientes, start=1):
        print(f"{i}. {p['nome']} - {p['idade']} anos - {p['telefone']}")

# Função principal (menu)
def menu():
    while True:
        print("\n=== SISTEMA CLÍNICA VIDA+ ===")
        print("1. Cadastrar paciente")
        print("2. Ver estatísticas")
        print("3. Buscar paciente")
        print("4. Listar todos os pacientes")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_paciente()
        elif opcao == "2":
            ver_estatisticas()
        elif opcao == "3":
            buscar_paciente()
        elif opcao == "4":
            listar_pacientes()
        elif opcao == "5":
            print("👋 Encerrando o sistema... Até logo!")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.")

# Inicia o programa
menu()
