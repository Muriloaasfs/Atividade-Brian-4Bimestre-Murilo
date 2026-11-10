# Superclasse
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


# Subclasse
class Carro(Veiculo):
    def __init__(self, marca, modelo, qtd_portas):
        super().__init__(marca, modelo)
        self.qtd_portas = qtd_portas


# Teste

meu_carro = Carro("Toyota", "Corolla", 4)

print(f"Marca: {meu_carro.marca}")
print(f"Modelo: {meu_carro.modelo}")
print(f"Quantidade de portas: {meu_carro.qtd_portas}")