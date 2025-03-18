import datetime
from abc import ABC, abstractmethod

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
        pass  # Implementação futura

class Saque(Transacao):
    def __init__(self, valor: float):
        self.valor = valor
    
    def registrar(self, conta):
        pass  # Implementação futura

# ==========================
# Classe de Histórico
# ==========================
class Historico:
    def __init__(self):
        self.transacoes = []
    
    def adicionar_transacao(self, transacao: Transacao):
        self.transacoes.append(transacao)

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
        pass  # Implementação futura
    
    def depositar(self, valor: float) -> bool:
        pass  # Implementação futura

class ContaCorrente(Conta):
    def __init__(self, cliente, numero: int, agencia: str, limite: float, limite_saques: int):
        super().__init__(cliente, numero, agencia)
        self.limite = limite
        self.limite_saques = limite_saques

# ==========================
# Classes de Cliente
# ==========================
class Cliente:
    def __init__(self, endereco: str):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        pass  # Implementação futura
    
    def adicionar_conta(self, conta: Conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf: str, nome: str, data_nascimento: datetime.date, endereco: str):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento