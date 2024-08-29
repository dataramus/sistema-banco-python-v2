# Sistema Bancário Simples Versão 2

## Sobre o Projeto:
Este é o 1° desafio do NTT DATA - Engenharia de Dados com Python da DIO.

## Visão Geral

Este projeto implementa um sistema bancário simples utilizando Python. Ele permite que os usuários realizem operações bancárias básicas, como depósitos, saques, visualização de histórico de transações (extrato), criação de novas contas e registro de novos usuários. O sistema foi projetado para ser uma aplicação de interface de linha de comando (CLI), demonstrando habilidades básicas de programação em Python, incluindo design de funções, manipulação de entradas, condicionais e estruturas de dados como listas e dicionários.

## Funcionalidades

- **Depósito**: Os usuários podem depositar dinheiro em sua conta, e a transação é registrada no extrato.
- **Saque**: Os usuários podem sacar dinheiro de sua conta, sujeito ao saldo disponível e aos limites de saque.
- **Visualizar Extrato**: Os usuários podem visualizar o saldo da conta e um histórico detalhado de transações.
- **Criar Nova Conta**: Novas contas bancárias podem ser criadas e vinculadas a usuários existentes.
- **Registrar Novo Usuário**: Novos usuários podem ser registrados utilizando seus dados pessoais.
- **Listar Todas as Contas**: Exibe todas as contas bancárias, incluindo detalhes como agência, número da conta e titular.

## Como Funciona

A aplicação opera em um loop, apresentando um menu ao usuário e realizando as operações selecionadas. Ela lida com cenários bancários comuns, como verificar a suficiência de fundos antes de permitir um saque e limitar o número de saques diários.

### Opções do Menu

- **[d] Depósito**: Adicionar fundos à sua conta.
- **[s] Saque**: Sacar fundos da sua conta, com verificações de saldo e limites.
- **[e] Visualizar Extrato**: Exibir o saldo atual e o histórico de transações.
- **[nc] Nova Conta**: Criar uma nova conta bancária associada a um usuário.
- **[lc] Listar Contas**: Ver todas as contas bancárias.
- **[nu] Novo Usuário**: Registrar um novo usuário no sistema.
- **[q] Sair**: Sair da aplicação.

## Instalação & Uso

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seuusuario/sistema-banco-python-v2.git
   cd sistema-bancario-simples
   ```

2. **Execute a aplicação:**

   Para iniciar a aplicação, basta rodar o script Python:

   ```bash
   python sisbanco_v2.py
   ```

3. **Siga as instruções na tela** para realizar operações bancárias.

## Visão Geral do Código

### Principais Funções

- `menu()`: Exibe o menu principal e captura a entrada do usuário.
- `depositar(saldo, valor, extrato)`: Realiza depósitos e atualiza o saldo e o histórico de transações do usuário.
- `sacar(saldo, valor, extrato, limite, num_saques, limite_saques)`: Gerencia saques com verificações de saldo disponível, limites e número de transações.
- `exibir_extrato(saldo, extrato)`: Exibe o saldo atual e o histórico de transações do usuário.
- `novo_usuario(usuarios)`: Registra um novo usuário com suas informações pessoais.
- `filtrar_usuario(cpf, usuarios)`: Busca um usuário pelo CPF (identificador único).
- `criar_conta(agencia, numero_conta, usuarios)`: Cria uma nova conta bancária para um usuário existente.
- `list_contas(contas)`: Lista todas as contas bancárias e seus detalhes.

### Estruturas de Dados

- **Usuários**: Armazenados em uma lista de dicionários, onde cada dicionário contém informações do usuário (ex.: nome, CPF, endereço).
- **Contas**: Armazenadas em uma lista de dicionários, onde cada dicionário representa uma conta e inclui detalhes como número da conta e informações do usuário.
- **Transações**: O histórico de transações é mantido como uma string que é atualizada a cada depósito ou saque.

## Contato

sinta-se à vontade para entrar em contato :)

- **Email**: coelho.lh@outlook.com
- **LinkedIn**: https://www.linkedin.com/in/luis-coelho-913093116/

Muito Obrigado!
