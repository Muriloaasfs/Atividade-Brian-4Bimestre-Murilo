#classe do funcionario
class Funcionario:
    def __init__(self, nome, matricula, salario_base):
        self.nome = nome
        self.matricula = matricula
        self.__salario_base = salario_base

    def get_salario_base(self):
        return self.__salario_base

    def set_salario_base(self, novo_salario):
        if novo_salario > 0:
            self.__salario_base = novo_salario

    def calcular_salario_final(self):
        return self.__salario_base

#classe do gerente
class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario_base, bonus_gestao):
        super().__init__(nome, matricula, salario_base)
        self.bonus_gestao = bonus_gestao

    def calcular_salario_final(self):
        return self.get_salario_base() + self.bonus_gestao

#classe do desenvolvedor
class Desenvolvedor(Funcionario):
    def __init__(self, nome, matricula, salario_base, nivel):
        super().__init__(nome, matricula, salario_base)
        self.nivel = nivel
#aí pra calcular o valor final
    def calcular_salario_final(self):
        if self.nivel == "Senior":
            return self.get_salario_base() + 1500
        else:
            return self.get_salario_base()



#fazer testes com as classes q foram criadas
#os valores de um gerente
gerente = Gerente(
    "Carlos Sei Lá",
    "001",
    8000,
    2000
)

#desenvolvedor
desenvolvedor = Desenvolvedor(
    "Ana",
    "001",
    4000,
    "Senior"
)

#tentar mudar o atributo pelo codigo
gerente.__salario_base = -100

#vendo o salario
print("Salário base do gerente:", gerente.get_salario_base())

#e mostrando o resultado dos salarios
print("Nome:", gerente.nome)
print("Salário final:", gerente.calcular_salario_final())

print()

print("Nome:", desenvolvedor.nome)
print("Salário final:", desenvolvedor.calcular_salario_final())

#aeeee deu certoo