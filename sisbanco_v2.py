# Este código em Python implementa um sistema bancário simples com várias funcionalidades, 
# Incluindo depósito, saque, exibição de extrato, criação de contas e usuários, e listagem de contas.

import textwrap

# A função menu exibe um menu de operações disponíveis para o usuário e retorna a opção escolhida.
def menu():
    menu = """
    ----------------- MENU ------------------
    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [nc] Nova Conta
    [lc] Lista Contas
    [nu] Novo Usuário
    [q]  Sair
    => """
    return input(textwrap.dedent(menu))

# A função depositar recebe o saldo atual, o valor do depósito e o extrato. Ela atualiza o valor.
# Caso o valor seja inválido, exibirá uma mensagem de erro.
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n Depósito Realizado. ")
    else:
        print("\n Operação Inválida. ")
    return saldo, extrato


# A função sacar realiza o saque, verifica se o valor solicitado é válido e se não ultrapassou os limites de saque e saldo.
def sacar(*, saldo, valor, extrato, limite, num_saques, limite_saques):
    sem_saldo = valor > saldo
    sem_limite = valor > limite
    sem_saque = num_saques >= limite_saques

    if sem_saldo:
        print("\n Saldo Insuficiente. ")
    elif sem_limite:
        print("\n Sem Limite. ")
    elif sem_saque:
        print("\n Número de Saques Excedido. ")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        num_saques += 1
        print("\n Saque Realizado ")
    else:
        print("\n Operação Inválida ")
    return saldo, extrato

# A função exibir_extrato exibe todas as transações realizadas e o saldo atual
def exibir_extrato(saldo, *, extrato):
    print("\n------------------------ EXTRATO ----------------------")
    print("Não Foram Realizadas Movimentações." if not extrato else extrato)
    print(f"\n Saldo: R$ {saldo:.2f}")
    print("---------------------------------------------------------")

# A função novo_usuário permite o cadastro de um novo usuário. O cadastro será vinculado ao CPF do usuário
def novo_usuario(usuarios):
    cpf = input("CPF (22222222222): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Usuário já cadastrado ")
        return
    
    nome = input("Nome Completo: ")
    data_nascimento = input("Digite a data de nascimento: (dd-mm-aaaa): ")
    endereco = input("Digite o Endereco")
    bairro = input("Digite o Bairro: ")
    cidade = input("Digite a Cidade: ")
    uf = input("Digite o Estado: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco, "bairro": bairro, "cidade": cidade, "estado": uf})

    print("\n Usuário Cadastrado com Sucesso ")

# A função filtrar_usuário busca usuário na lista de usuários cadastrados, o CPF é a chave de busca
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

# A função criar_conta cria uma conta a um usuário existente.
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n Conta criada com sucesso! ")
        return {"agencia": agencia, "num_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não encontrado. ")

# A função list_contas lista todas as contas criadas, exibindo detalhes como a agência, números da conta, e o titular.
def list_contas(contas):
    for conta in contas:
        linha = f"""
                    Agência: {conta['agencia']}
                    Conta: {conta['num_conta']}
                    Titular: {conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

# A função main é a função principal do programa, ela controla o loop do menu.
# Ela chama as funções com base na entrada do menu.def main():
    LIM_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    num_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                num_saques=num_saques,
                limite_saques=LIM_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            novo_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            list_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida.")

