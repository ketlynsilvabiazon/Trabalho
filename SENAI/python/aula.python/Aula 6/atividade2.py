# ATIVIDADE 2

# Criar uma estrutura para controlar as contas em um banco

# Você pode ter Conta corrente, poupança
# A classe escolhida entre as 2, herdam da classe Conta

# Métodos de sacar, depositar, extrato (movimentações / lista)
# Transferir (colocar a conta de destino)
# Fechar a conta (precisa estar com o saldo em 0)

# Atributos como: Titular, Saldo

# ex:
# conta1.transferir(500, conta2)




class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.extrato = []

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.append(f"Depósito: R${valor}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"Saque: R${valor}")
        else:
            print("Saldo insuficiente!")

    def transferir(self, valor, conta):
        if valor <= self.saldo:
            self.saldo -= valor
            conta.saldo += valor
            self.extrato.append(f"Transferiu R${valor} para {conta.titular}")
            conta.extrato.append(f"Recebeu R${valor} de {self.titular}")
        else:
            print("Saldo insuficiente!")

    def mostrar_extrato(self):
        print(f"\nExtrato de {self.titular}")
        if len(self.extrato) == 0:
            print("Nenhuma movimentação.")
        else:
            for mov in self.extrato:
                print(mov)
        print(f"Saldo: R${self.saldo}")

    def fechar_conta(self):
        if self.saldo == 0:
            print("Conta fechada com sucesso!")
        else:
            print("A conta só pode ser fechada com saldo igual a 0.")


class ContaCorrente(Conta):
    pass


class ContaPoupanca(Conta):
    pass



nome1 = input("Nome do titular da Conta Corrente: ")
saldo1 = float(input("Saldo inicial: "))
conta1 = ContaCorrente(nome1, saldo1)

nome2 = input("\nNome do titular da Conta Poupança: ")
saldo2 = float(input("Saldo inicial: "))
conta2 = ContaPoupanca(nome2, saldo2)


while True:
    print("\n===== MENU =====")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Transferir")
    print("4 - Mostrar Extrato")
    print("5 - Fechar Conta")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        conta = input("Depositar em qual conta? (1-Corrente / 2-Poupança): ")
        valor = float(input("Valor do depósito: "))

        if conta == "1":
            conta1.depositar(valor)
        elif conta == "2":
            conta2.depositar(valor)

    elif opcao == "2":
        conta = input("Sacar de qual conta? (1-Corrente / 2-Poupança): ")
        valor = float(input("Valor do saque: "))

        if conta == "1":
            conta1.sacar(valor)
        elif conta == "2":
            conta2.sacar(valor)

    elif opcao == "3":
        print("\nQual conta vai transferir?")
        print("1 - Conta Corrente")
        print("2 - Conta Poupança")

        origem = input("Escolha: ")
        valor = float(input("Valor da transferência: "))

        if origem == "1":
            conta1.transferir(valor, conta2)
        elif origem == "2":
            conta2.transferir(valor, conta1)
        else:
            print("Opção inválida!")

    elif opcao == "4":
        conta1.mostrar_extrato()
        conta2.mostrar_extrato()

    elif opcao == "5":
        conta = input("Qual conta deseja fechar? (1-Corrente / 2-Poupança): ")

        if conta == "1":
            conta1.fechar_conta()
        elif conta == "2":
            conta2.fechar_conta()

    elif opcao == "0":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")