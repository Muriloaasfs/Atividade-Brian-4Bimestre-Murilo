from abc import ABC, abstractmethod


class Veiculo(ABC):
    def __init__(self, modelo):
        self.modelo = modelo

    @abstractmethod
    def acelerar(self):
        pass


class Carro(Veiculo):
    def acelerar(self):
        print(f"Carro {self.modelo} acelerando pela pista!")


class Moto(Veiculo):
    def acelerar(self):
        print(f"Moto {self.modelo} acelerando rapidamente!")


class Caminhao(Veiculo):
    def acelerar(self):
        print(f"Caminhão {self.modelo} acelerando com muita força!")


class CarroEletrico(Veiculo):
    def acelerar(self):
        print(f"Carro elétrico {self.modelo} acelerando silenciosamente!")


pista_de_corrida = [
    Carro("Civic"),
    Moto("CB 500"),
    Caminhao("Volvo FH"),
    CarroEletrico("Tesla Model 3")
]


for veiculo in pista_de_corrida:
    veiculo.acelerar()
