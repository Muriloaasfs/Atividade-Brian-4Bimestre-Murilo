class Veiculo:
    def __init__(self, modelo, placa, valor_diaria):
        self.set_modelo(modelo)
        self.set_placa(placa)
        self.set_valor_diaria(valor_diaria)

#aqui define as diferentes funcoes que vm usar depois
    def get_modelo(self):
        return self.__modelo

    def get_placa(self):
        return self.__placa

    def get_valor_diaria(self):
        return self.__valor_diaria

    def set_modelo(self, modelo):
        if modelo == "":
            raise ValueError("Modelo inválido")
        self.__modelo = modelo

    def set_placa(self, placa):
        if placa == "":
            raise ValueError("Placa inválida")
        self.__placa = placa

    def set_valor_diaria(self, valor):
        if valor <= 0:
            raise ValueError("Valor inválido")
        self.__valor_diaria = valor

    def calcular_aluguel(self, dias):
        if dias <= 0:
            raise ValueError("Quantidade de dias inválida")
        return self.__valor_diaria * dias

#aqui cria a classe carros
class Carro(Veiculo):
    def __init__(self, modelo, placa, valor_diaria, portas):
        super().__init__(modelo, placa, valor_diaria)
        self.__portas = portas

    def get_portas(self):
        return self.__portas

    def calcular_aluguel(self, dias):
        return super().calcular_aluguel(dias) + 50

#e aqui a de motos
class Moto(Veiculo):
    def __init__(self, modelo, placa, valor_diaria, cilindradas):
        super().__init__(modelo, placa, valor_diaria)
        self.__cilindradas = cilindradas

    def get_cilindradas(self):
        return self.__cilindradas

    def calcular_aluguel(self, dias):
        return super().calcular_aluguel(dias) * 0.90

#daqui pra baixo é pra mostrar os resultados
veiculos = []
#com os numeros pra organnizar melhor prof
while True:
    print("\n1 - Cadastrar carro")
    print("2 - Cadastrar moto")
    print("3 - Listar veículos")
    print("4 - Calcular aluguel")
    print("5 - Sair")

    try:
        escolha = int(input("Escolha: "))

        if escolha == 1:
            modelo = input("Modelo: ")
            placa = input("Placa: ")
            valor = float(input("Valor da diária: "))
            portas = int(input("Portas: "))

            veiculos.append(Carro(modelo, placa, valor, portas))
            print("Carro cadastrado")

        elif escolha == 2:
            modelo = input("Modelo: ")
            placa = input("Placa: ")
            valor = float(input("Valor da diária: "))
            cilindradas = int(input("Cilindradas: "))

            veiculos.append(Moto(modelo, placa, valor, cilindradas))
            print("Moto cadastrada")

        elif escolha == 3:
            if len(veiculos) == 0:
                print("Nenhum veículo cadastrado")
            else:
                for veiculo in veiculos:
                    print("\nModelo:", veiculo.get_modelo())
                    print("Placa:", veiculo.get_placa())
                    print("Diária:", veiculo.get_valor_diaria())

                    if isinstance(veiculo, Carro):
                        print("Portas:", veiculo.get_portas())
                    else:
                        print("Cilindradas:", veiculo.get_cilindradas())

        elif escolha == 4:
            dias = int(input("Dias: "))

            for veiculo in veiculos:
                print(
                    veiculo.get_modelo(),
                    "- R$",
                    f"{veiculo.calcular_aluguel(dias):.2f}"
                )

        elif escolha == 5:
            print("Fim do programa")
            break

        else:
            print("Escolha inválida")

    except ValueError as erro:
        print("Erro:", erro)

    else:
        print("Operação realizada com sucesso")

    finally:
        print("Operação encerrada")