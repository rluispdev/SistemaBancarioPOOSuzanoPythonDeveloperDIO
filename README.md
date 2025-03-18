![Template rluipdev](rluispdev(4).png)

# Criando um Sistema Bancário 2 com Python

## Descrição

Neste desafio do BootCamp Suzano - Python Developer na DIO, o objetivo foi criar um sistema bancário simples utilizando a linguagem Python e Programação Orientada a Objetos (POO). O sistema permite realizar operações bancárias com validações e regras de negócios, como:

- **Criação de Conta Corrente**: Permite a criação de contas correntes com limites de saque e depósito diários.
- **Depósito**: Permite ao usuário realizar depósitos em sua conta, com um limite diário de depósitos.
- **Saque**: Realiza saques, respeitando um limite diário de saques e verificando se o saldo é suficiente.
- **Extrato**: Exibe um histórico completo de transações realizadas (depósitos e saques), junto ao saldo atual.

O código foi estruturado de maneira a aplicar os conceitos de **POO** (encapsulamento, herança e polimorfismo), facilitando a manutenção e evolução do sistema.

---

## Objetivos do Projeto

1. **Operação de Depósito**
   - Permitir que o usuário deposite valores positivos.
   - Armazenar os depósitos em uma variável e exibi-los na operação de extrato.
   - Garantir que o valor do depósito seja maior que zero.

2. **Operação de Saque**
   - Permitir que o usuário realize até três saques diários, com um limite de R$ 500,00 por saque.
   - Exibir uma mensagem caso o saldo seja insuficiente para o saque ou se o valor ultrapassar o limite permitido.

3. **Operação de Extrato**
   - Listar todos os depósitos e saques realizados na conta.
   - Exibir o saldo atual da conta de forma formatada.

---

## Tecnologias e Ferramentas

- **Linguagem**: Python 3.x
- **Paradigma**: Programação Orientada a Objetos (POO)
- **Imports**:
- **Imports**:
  - `import datetime`: Utilizado para controlar as datas e horários das transações, como o registro de depósitos e saques.
  - `import os`: Usado para manipulação de operações do sistema operacional, como limpeza de tela ou verificações de arquivos.
  - `from abc import ABC, abstractmethod`: Usado para criar classes abstratas, permitindo a definição de interfaces e garantindo que as subclasses implementem métodos específicos.
  
- **IDE/Editor**: Pode ser utilizado qualquer editor de texto como VSCode, PyCharm ou até mesmo o terminal/console para execução.
- **Bibliotecas**: Nenhuma biblioteca externa foi necessária, utilizando apenas funcionalidades nativas do Python.

---

## Estrutura do Código

- **Classe ContaCorrente**: Representa a conta bancária e contém métodos para realizar depósitos, saques e exibir extrato.
- **Classe Usuario**: Representa o cliente do banco e é responsável por armazenar suas informações e realizar operações bancárias.
- **Métodos**: Implementados como funções dentro das classes para tratar o comportamento das operações de depósito, saque e extrato.

---

## Como Executar

1. Clone este repositório:
   ```bash
    https://github.com/rluispdev/SistemaBancarioPOOSuzanoPythonDeveloperDIO



  2.	Execute o arquivo main.py ou o arquivo que contiver o código principal.
	3.	Siga as instruções no terminal para realizar depósitos, saques e consultar o extrato.


## Instrutor

- Guilherme Arthur de Carvalho - Analista de Sistemas


<p>
    <img 
      align=left 
      margin=10 
      width=80 
      src="https://avatars.githubusercontent.com/u/128305083?s=96&v=4"
    />
    <p>&nbsp&nbsp&nbsprluispdev<br>
    &nbsp&nbsp&nbsp
    <a href="https://github.com/rluispdev">
    GitHub</a>&nbsp;|&nbsp;
     <a href="https://cursos.alura.com.br/user/rluisp"> Alura Profile</a>
&nbsp;|&nbsp;
       <a href="https://www.dio.me/users/rluispdev">DIO</a>
&nbsp;|&nbsp;      
    <a href="https://www.linkedin.com/in/rafael-luis-gonzaga-b11634186/">LinkedIn</a>
&nbsp;|&nbsp;
    <a href="https://www.instagram.com/rluispdevs?igsh=cnoxenpmaHY1amE0&utm_source=qr">
    Instagram</a>
&nbsp;|&nbsp;</p>
</p>
<br/><br/>
<p>
 

