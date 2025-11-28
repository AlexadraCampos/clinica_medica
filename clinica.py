from collections import deque

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

# Função para buscar paciente
def buscar_paciente():
    print("\n=== BUSCAR PACIENTE ===")
    nome_busca = input("Digite o nome do paciente: ").strip().title()
    encontrados = [p for p in pacientes if nome_busca in p["nome"]]

    if encontrados:
        for p in encontrados:
            print(f"👤 Nome: {p['nome']} | Idade: {p['idade']} | Telefone: {p['telefone']}")
    else:
        print("❌ Paciente não encontrado.")

# Função para listar pacientes
def listar_pacientes():
    print("\n=== LISTA DE PACIENTES ===")
    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado.")
        return

    for i, p in enumerate(pacientes, start=1):
        print(f"{i}. {p['nome']} - {p['idade']} anos - {p['telefone']}")

# === CONTROLE DE ACESSO ===
def controle_acesso():
    print("\n=== CONTROLE DE ACESSO AO ATENDIMENTO ===")

    # Entrada dos dados
    A = input("Tem agendamento? (s/n): ").lower() == "s"
    B = input("Documentos em dia (RG/CPF válidos)? (s/n): ").lower() == "s"
    C = input("Há médico disponível? (s/n): ").lower() == "s"
    D = input("Pagamentos em dia? (s/n): ").lower() == "s"

    consulta_normal = (A and B and C) or (B and C and D)
    emergencia = C and (B or D)

    print("\n--- RESULTADOS ---")
    print(f"Consulta Normal: {'✅ Pode ser atendido' if consulta_normal else '❌ Não pode ser atendido'}")
    print(f"Emergência: {'✅ Pode ser atendido' if emergencia else '❌ Não pode ser atendido'}")


def situacao_pratica():
    print("\n=== SITUAÇÃO PRÁTICA ===")
    print("A=F (Sem agendamento), B=V (Documentos OK), C=V (Médico disponível), D=F (Pagamentos atrasados)")

    A, B, C, D = False, True, True, False

    consulta_normal = (A and B and C) or (B and C and D)
    emergencia = C and (B or D)

    print(f"Consulta Normal: {'✅ Atendido' if consulta_normal else '❌ Não atendido'}")
    print(f"Emergência: {'✅ Atendido' if emergencia else '❌ Não atendido'}")

# === FILA DE ATENDIMENTO ===
fila = deque()

def fila_atendimento():
    print("\n=== FILA DE ATENDIMENTO ===")
    
    for i in range(3):
        nome = input(f"Digite o nome do {i+1}º paciente: ").title().strip()
        cpf = input("Digite o CPF: ").strip()
        fila.append({"nome": nome, "cpf": cpf})

    print("\nFila inicial:")
    for p in fila:
        print(f"- {p['nome']} ({p['cpf']})")

    if fila:
        atendido = fila.popleft()
        print(f"\n🩺 Paciente em atendimento: {atendido['nome']}")
    
    if fila:
        print("\n📋 Pacientes que ainda aguardam:")
        for p in fila:
            print(f"- {p['nome']} ({p['cpf']})")
    else:
        print("\n✅ Todos os pacientes foram atendidos.")

# === MENU PRINCIPAL ===
def menu():
    while True:
        print("\n=== SISTEMA CLÍNICA VIDA+ ===")
        print("1. Cadastrar paciente")
        print("2. Ver estatísticas")
        print("3. Buscar paciente")
        print("4. Listar pacientes")
        print("5. Controle de acesso")
        print("6. Fila de atendimento")
        print("7. Sair")

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
            controle_acesso()
        elif opcao == "6":
            fila_atendimento()
        elif opcao == "7":
            print("Encerrando o sistema... Até logo!")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.")

# Inicia o programa
menu()
