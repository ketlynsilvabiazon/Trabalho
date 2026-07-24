# # Orirntaçao de objetos
# Orientação a Objetos



# EXEMPLO 1



# class Casa:   # Molde
#     def __init__(self, cor, area, rua): # Método construtor
#         self.cor = cor    # Atributos
#         self.rua = rua
#         self.area = area

    
#     def pintarCasa(self, novaCor): # Método padrão
#         self.cor = novaCor


# joao = Casa('Azul', 50, 'general portiguara')  # Objeto instanciado da classe Casa
# # joao.rua = "teste"         # mudar o valor diretamente
# # joao.pintarCasa('Azul')    # mudar o valor de maneira robusta
# print(joao.cor)

# maria = Casa('Azul', 100, 'acioly filho')
# print(maria.rua)




# EXEMPLO 2



# class ContaCorrente: #Molde
#     def __init__(self, dono):
#         self.saldo = 0            #Atributos
#         self.titular = dono
#         self.ativo = True

#     def depositar(self,valor):    #Metodo padrao
#         self.saldo += valor

# #     def sacar(self, valor):
# #         if valor > self.saldo:
# #             print('saldo Insuficiente')
# #         else:
# #             self.saldo -= valor
# #             print('Retirado: R$', valor)
# #             print('Saldo Restante: R$', self.saldo)

# # conta1 = ContaCorrente('Donathan') #Objeto instanciado da classe
# # conta2 = ContaCorrente('Maria')

# # conta1.depositar(500)
# # conta2.depositar(500)

# # conta1.sacar(200)
# # conta2.sacar(200)
