#classe da Pessoa
class Pessoa:
    def __init__(self, nome, cpf, mensalidade_base):
        self._nome = nome
        self._cpf = cpf
        self._mensalidade_base = mensalidade_base

    def calcular_pagamento(self):
        return self._mensalidade_base


# do Aluno
class Aluno(Pessoa):
    def __init__(self, nome, cpf, mensalidade_base, nota_desempenho):
        super().__init__(nome, cpf, mensalidade_base)
        self._nota_desempenho = nota_desempenho

    # Sobrescrita do método calcular_pagamento
    def calcular_pagamento(self):
        if self._nota_desempenho >= 9.0:
            return self._mensalidade_base * 0.80
        else:
            return self._mensalidade_base


#do Prof
class Professor(Pessoa):
    def __init__(self, nome, cpf, mensalidade_base, horas_extras):
        super().__init__(nome, cpf, mensalidade_base)
        self._horas_extras = horas_extras

    #definir como paga o proff
    def calcular_pagamento(self):
        return self._mensalidade_base + (self._horas_extras * 40)


#e como mostra o resultado
def exibir_relatorio_financeiro(pessoa):
    print("\n===== RELATÓRIO FINANCEIRO =====")
    print(f"Nome: {pessoa._nome}")
    print(f"CPF: {pessoa._cpf}")
    print(f"Valor final: R$ {pessoa.calcular_pagamento():.2f}")
    print("================================")


#ler os numero que sao positivos
def ler_float_positivo(mensagem):
    while True:
        try:
            valor = float(input(mensagem))

            if valor > 0:
                return valor
            else:
                print("Digite um valor maior que zero.")

        except ValueError:
            print("Valor inválido! Digite apenas números.")


#e como q calula tudo
def main():

    print("===== SISTEMA DE GESTÃO ESCOLAR =====")

    try:
        print("\n--- Cadastro do Aluno ---")

        nome_aluno = input("Nome do aluno: ")
        cpf_aluno = input("CPF do aluno: ")

        mensalidade_aluno = ler_float_positivo(
            "Mensalidade base do aluno: R$ "
        )

        nota_aluno = ler_float_positivo(
            "Nota de desempenho do aluno: "
        )

        aluno = Aluno(
            nome_aluno,
            cpf_aluno,
            mensalidade_aluno,
            nota_aluno
        )

        print("\n--- Cadastro do Professor ---")

        nome_professor = input("Nome do professor: ")
        cpf_professor = input("CPF do professor: ")

        salario_professor = ler_float_positivo(
            "Valor base do professor: R$ "
        )

        horas_extras = int(
            ler_float_positivo("Quantidade de horas extras: ")
        )

        professor = Professor(
            nome_professor,
            cpf_professor,
            salario_professor,
            horas_extras
        )

        #pra mostrar os resultados
        print("\n\nRELATÓRIOS")

        exibir_relatorio_financeiro(aluno)
        exibir_relatorio_financeiro(professor)

    except Exception as erro:
        print(f"\nOcorreu um erro durante a execução: {erro}")

    finally:
        print("\nGeração dos relatórios concluída.")
        print("Programa encerrado.")


#e fazer o programa rodar
if __name__ == "__main__":
    main()
