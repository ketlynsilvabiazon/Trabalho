# # ATIVIDADE 1
# # Criar a classe Carro
# # Métodos: Acelerar, Freiar, Ligar, Desligar



class Carro:
    def __init__(self):
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if self.ligado:
            print('O carro já está ligado ')
        else:
            self.ligado = True
            print('Carro ligado')
        
    def desligar(self):
        if self.velocidade == 0:
            self.ligado = False
            print('Carro desligado')   
        else:
            print('Pare o carro antes de desligar')

    def acelerar(self):
        if self.ligado:
            self.velocidade += 10
            print('Velocidade:', self.velocidade, 'km/h')
        else:
            print('Ligue o carro primeiro.')

    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 10
            print('Velocidade:', self.velocidade, 'km/h')
        else:
            print('O carro já está parado')

Carro = Carro()
Carro.ligar()
Carro.frear()
Carro.acelerar()
Carro.desligar()
