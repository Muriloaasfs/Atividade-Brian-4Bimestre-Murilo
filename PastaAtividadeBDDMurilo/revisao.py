class Veiculo
    def __init__(self, marca, modelo, valor_diaria):
        self.marca = marca
        self.moddelo = modelo
        self.__valor_diaria = valor_diaria
    def get_valor_diaria(self):
        return self.__valor_diaria
    def calcular_aluguel(self, dias):
        return self.get_valor_diaria() * dias

class Carro(Veiculo):
    def __init__(self, marca, modelo, valor_diaria, portas):
        super().__init__(marca, modelo, valor_diaria)
        self.portas = portas
    def calcular_aluguel(self, dias):
        val_base = super().calcular_aluguel(dias)
        return val_base + 50.0

class 

restante:

# ==============================================================================
# 1. ABSTRAÇÃO E ENCAPSULAMENTO (SUPERCLASSE)
# ==============================================================================
class Veiculo:
    def __init__(self, marca, modelo, valor_diaria):
        self.marca = marca
        self.modelo = modelo
        self.__valor_diaria = valor_diaria
    def get_valor_diaria(self):
        return self.__valor_diaria
    def calcular_aluguel(self, dias):
        return self.get_valor_diaria() * dias
# 2. HERANÇA E REUSO DE CÓDIGO (SUBCLASSE 1)
class Carro(Veiculo):
    def __init__(self, marca, modelo, valor_diaria, portas):
        super().__init__(marca, modelo, valor_diaria)  # Reuso com super()
        self.portas = portas
    def calcular_aluguel(self, dias):
        # Sobrescrita com taxa adicional
        val_base = super().calcular_aluguel(dias)
        return val_base + 50.0
# ==============================================================================
# 3. SOBRESCRITA DE MÉTODOS (SUBCLASSE 2)
# ==============================================================================
class Moto(Veiculo):
    def __init__(self, marca, modelo, valor_diaria, cilindradas):
        # TODO: Chame o construtor da superclasse usando o super()
        
        self.cilindradas = cilindradas

 

    # TODO: SOBRESCREVA o método 'calcular_aluguel(self, dias)'
    # Regra: A Moto tem um desconto de 10% no valor total do aluguel.
    def calcular_aluguel(self, dias):
        pass


 

# ==============================================================================
# 4. TESTE DE POLIMORFISMO E EXECUÇÃO (MAIN)
# ==============================================================================
# Instanciando os objetos (Já fornecido):
carro1 = Carro("Toyota", "Corolla", 150.0, 4)
moto1 = Moto("Honda", "CB 500", 100.0, 500)

 

# TODO: Crie uma lista chamada 'frota' contendo os dois objetos acima (carro1 e moto1)
frota = []

 

# TODO: Escreva um laço 'for' que percorra a lista 'frota' e imprima o valor do aluguel para 3 dias de cada veículo.
# DICA: Execute o método 'calcular_aluguel(3)' de forma genérica para cada item!
print("--- RESUMO DOS ALUGUÉIS (3 DIAS) ---")
for veiculo in frota:
    # Digite a chamada polimórfica aqui
    pass


 

# ==============================================================================
# 5. TESTE DE REVISÃO DO NAME MANGLING (DESAFIO DE ATENÇÃO)
# ==============================================================================
# TODO: Tente alterar a diária do carro diretamente executando a linha abaixo.
# Depois, execute o print para verificar se o valor REAL do atributo privado mudou ou não.

 

carro1.__valor_diaria = 10.0 # Tentativa de alteração direta
print("\nO valor da diária mudou para 10.0?")
print("Valor lido pelo Getter:", carro1.get_valor_diaria()) 
# Pergunta de Prova: O valor vai ser 10.0 ou 150.0?

# NA TEORIA CORRIGIDO:
# ==============================================================================
# 3. SOBRESCRITA DE MÉTODOS (SUBCLASSE 2)
# ==============================================================================
class Moto(Veiculo):
    def __init__(self, marca, modelo, valor_diaria, cilindradas):
        # Chama o construtor da superclasse usando super()
        super().__init__(marca, modelo, valor_diaria)
        
        self.cilindradas = cilindradas

    # Sobrescreve o método calcular_aluguel
    # A Moto tem um desconto de 10% no valor total do aluguel.
    def calcular_aluguel(self, dias):
        val_base = super().calcular_aluguel(dias)
        return val_base * 0.90


# ==============================================================================
# 4. TESTE DE POLIMORFISMO E EXECUÇÃO (MAIN)
# ==============================================================================
# Instanciando os objetos
carro1 = Carro("Toyota", "Corolla", 150.0, 4)
moto1 = Moto("Honda", "CB 500", 100.0, 500)

# Cria uma lista contendo os dois objetos
frota = [carro1, moto1]

# Percorre a lista e calcula o aluguel de cada veículo para 3 dias
print("--- RESUMO DOS ALUGUÉIS (3 DIAS) ---")
for veiculo in frota:
    print("Valor do aluguel:", veiculo.calcular_aluguel(3))


# ==============================================================================
# 5. TESTE DE REVISÃO DO NAME MANGLING (DESAFIO DE ATENÇÃO)
# ==============================================================================
# Tentativa de alterar a diária do carro diretamente
carro1.__valor_diaria = 10.0

print("\nO valor da diária mudou para 10.0?")
print("Valor lido pelo Getter:", carro1.get_valor_diaria())

# Pergunta de Prova:
# O valor será 10.0