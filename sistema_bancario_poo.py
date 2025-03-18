import datetime
import os
from abc import ABC, abstractmethod

# ==========================
# Limites Globais
# ==========================
LIMITE_SAQUES_DIARIOS = 5  # Limite de saques diários
LIMITE_DEPOSITO_DIARIO = 10000.0  # Limite de depósito diário
LIMITE_SAQUE_DIARIO = 5000.0  # Limite de saque diário fixo
LIMITE_TRANSACOES_DIARIAS = 10  # Limite de transações por dia (inclui criação de conta, saques e depósitos)
LIMITE_CONTAS_DIARIAS = 2  # Limite de contas a serem criadas por dia
contas_criadas_no_dia = 0  # Contador global para contas criadas

# ==========================
# Classes de Transação
# ==========================
class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor: float):
        self.valor = valor
    
    def registrar(self, conta):
        if self.valor > 0:
            conta.saldo += self.valor
            conta.historico.adicionar_transacao(f"Depósito de R$ {self.valor:.2f}")
            return True
        return False

class Saque(Transacao):
    def __init__(self, valor: float):
        self.valor = valor
    
    def registrar(self, conta):
        if 0 < self.valor <= conta.saldo:
            conta.saldo -= self.valor
            conta.historico.adicionar_transacao(f"Saque de R$ {self.valor:.2f}")
            return True
        return False

# ==========================
# Classe de Histórico
# ==========================
class Historico:
    def __init__(self):
        self.transacoes = []
    
    def adicionar_transacao(self, descricao: str):
        data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.transacoes.append(f"[{data_hora}] {descricao}")
    
    def exibir_extrato(self):
        return "\n".join(self.transacoes) if self.transacoes else "Nenhuma movimentação realizada."

# ==========================
# Classes de Conta
# ==========================
class Conta:
    def __init__(self, cliente, numero: int, agencia: str):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()
    
    def saldo(self):
        return self.saldo
    
    def sacar(self, valor: float) -> bool:
        saque = Saque(valor)
        return saque.registrar(self)
    
    def depositar(self, valor: float) -> bool:
        deposito = Deposito(valor)
        return deposito.registrar(self)

class ContaCorrente(Conta):
    LIMITE_SAQUES_DIARIOS = 3
    
    def __init__(self, cliente, numero: int, agencia: str, limite_deposito_diario: float):
        super().__init__(cliente, numero, agencia)
        self.limite = 5000.0  # Limite fixo de crédito
        self.saques_realizados = 0
        self.deposito_diario_realizado = 0.0
        self.limite_deposito_diario = limite_deposito_diario
    
    def sacar(self, valor: float) -> bool:
        # Verificar se o limite de transações diárias foi atingido
        if self.cliente.transacoes_diarias >= LIMITE_TRANSACOES_DIARIAS:
            print("Limite de transações diárias atingido.")
            return False
        
        # Verificar se o limite de saques diários foi atingido
        if self.saques_realizados >= ContaCorrente.LIMITE_SAQUES_DIARIOS:
            print("Limite de saques diário atingido.")
            return False
        
        # Verificar se o valor do saque é maior que o limite de saque diário
        if valor > LIMITE_SAQUE_DIARIO:
            print(f"Limite de saque diário de R$ {LIMITE_SAQUE_DIARIO:.2f} atingido.")
            return False
        
        # Verificar se o valor do saque é maior que o saldo disponível
        if valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
            return False
        
        # Verificar se o valor do saque é maior que o limite de crédito
        if valor > self.limite:
            print("Valor do saque ultrapassa o limite de crédito.")
            return False
        
        # Realizar o saque
        if super().sacar(valor):
            self.saques_realizados += 1
            self.cliente.transacoes_diarias += 1
            return True
        return False

    def depositar(self, valor: float) -> bool:
        # Verificar se o limite de transações diárias foi atingido
        if self.cliente.transacoes_diarias >= LIMITE_TRANSACOES_DIARIAS:
            print("Limite de transações diárias atingido.")
            return False
        
        # Verificar se o limite de depósito diário foi atingido
        if self.deposito_diario_realizado + valor > self.limite_deposito_diario:
            print(f"Limite de depósito diário de R$ {self.limite_deposito_diario:.2f} atingido.")
            return False
        
        # Realizar o depósito
        if super().depositar(valor):
            self.deposito_diario_realizado += valor
            self.cliente.transacoes_diarias += 1
            return True
        return False

# ==========================
# Classes de Cliente
# ==========================
class Cliente:
    def __init__(self, endereco: str):
        self.endereco = endereco
        self.contas = []
        self.transacoes_diarias = 0  # Contador de transações diárias
    
    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        # Verificar se o limite de transações diárias foi atingido
        if self.transacoes_diarias >= LIMITE_TRANSACOES_DIARIAS:
            print("Limite de transações diárias atingido.")
            return False
        sucesso = transacao.registrar(conta)
        if sucesso:
            self.transacoes_diarias += 1
        return sucesso
    
    def adicionar_conta(self, conta: Conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf: str, nome: str, data_nascimento: datetime.date, endereco: str):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

# ==========================================================================================================================

# Simulação a interação de um menu de terminal 

def exibir_menu():
    print("===================================")
    print("Bem-vindo ao Sistema Bancário!")
    print("1. Criar conta corrente")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Saldo")
    print("5. Exibir Extrato")
    print("6. Dados da Conta")
    print("7. Sair")
    print("===================================")

def criar_conta():
    global contas_criadas_no_dia
    if contas_criadas_no_dia >= LIMITE_CONTAS_DIARIAS:
        print("Limite de criação de contas atingido para hoje.")
        return None, None

    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    
    while True:
        data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
        try:
            data_nascimento = datetime.datetime.strptime(data_nascimento, "%d/%m/%Y").date()
            break  # Sai do loop se a data for válida
        except ValueError:
            print("Formato de data incorreto. Por favor, insira a data no formato DD/MM/AAAA.")
    
    cliente = PessoaFisica(cpf, nome, data_nascimento, endereco)
    numero_conta = int(input("Digite o número da conta: "))
    agencia = input("Digite o número da agência: ")
    
    conta_corrente = ContaCorrente(cliente, numero_conta, agencia, LIMITE_DEPOSITO_DIARIO)
    cliente.adicionar_conta(conta_corrente)
    contas_criadas_no_dia += 1
    
    # Limpa a tela 
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Exibe apenas a mensagem de sucesso
    print(f"\nConta Corrente criada com sucesso para {nome}.")
    
    return cliente, conta_corrente

def exibir_dados_conta(cliente):
    if cliente:
        # Verifica se o cliente tem contas e as exibe
        for conta in cliente.contas:
            print("===== Dados da Conta =====")
            print(f"Nome: {cliente.nome}")
            print(f"Agência: {conta.agencia}  Conta: {conta.numero}")
    else:
        print("Nenhum cliente cadastrado.")

def realizar_deposito(conta):
    valor = float(input("Digite o valor para depósito: R$ "))
    if conta.depositar(valor):
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Falha ao realizar o depósito.")

def realizar_saque(conta):
    valor = float(input("Digite o valor para saque: R$ "))
    if conta.sacar(valor):
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Falha ao realizar o saque.")

def exibir_extrato(conta):
    print("===== Extrato da Conta =====")
    print(conta.historico.exibir_extrato())

def exibir_saldo(conta):
    print(f"Saldo atual: R$ {conta.saldo:.2f}")

# ==========================
# Função principal
# ==========================
def obter_opcao():
    while True:
        entrada = input("Escolha uma opção: ").strip()
        if entrada.isdigit():  # Verifica se é um número válido
            return int(entrada)
        print("Opção inválida. Por favor, digite um número entre 1 e 7.")

def main():
    cliente, conta_corrente = None, None
    while True:
        exibir_menu()
        opcao = obter_opcao()
        
        if opcao == 1:
            cliente, conta_corrente = criar_conta()
        elif opcao == 2:
            if conta_corrente:
                realizar_deposito(conta_corrente)
            else:
                print("Conta não criada ainda.")
        elif opcao == 3:
            if conta_corrente:
                realizar_saque(conta_corrente)
            else:
                print("Conta não criada ainda.")
        elif opcao == 4:
            if conta_corrente:
                exibir_saldo(conta_corrente)
            else:
                print("Conta não criada ainda.")
        elif opcao == 5:
            if conta_corrente:
                exibir_extrato(conta_corrente)
            else:
                print("Conta não criada ainda.")
        elif opcao == 6:
            exibir_dados_conta(cliente)
        elif opcao == 7:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()