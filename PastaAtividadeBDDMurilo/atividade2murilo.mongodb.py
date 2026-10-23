class Aluno:
    """Classe base do sistema acadêmico (Passo 1: classe principal = Aluno)."""

    def __init__(self, nome, media):
        # Valores padrão seguros, usados caso o dado informado seja inválido
        self.__nome = "Não informado"
        self.__media = 0.0
        # __init__ redireciona para os setters (que validam)
        self.set_nome(nome)
        self.set_media(media)

    # ----- Getters -----
    def get_nome(self):
        return self.__nome

    def get_media(self):
        return self.__media

    # ----- Setters com validação -----
    def set_nome(self, nome):
        if isinstance(nome, str) and len(nome.strip()) >= 3:
            self.__nome = nome.strip()
        else:
            print("Erro: o nome deve ter pelo menos 3 caracteres.")

    def set_media(self, media):
        if isinstance(media, (int, float)) and 0 <= media <= 10:
            self.__media = float(media)
        else:
            print("Erro: a média deve estar entre 0 e 10.")


# ==============================================================================
# TESTE DE VALIDAÇÃO DO PROJETO FINAL
# ==============================================================================
if __name__ == "__main__":
    print("=== TESTANDO A CLASSE BASE DO PROJETO FINAL ===")

    # 1. Teste de Instanciação com dados VÁLIDOS
    objeto_valido = Aluno("Maria Silva", 8.5)
    print(f"Objeto Criado: {objeto_valido.get_nome()} - Média {objeto_valido.get_media():.2f}")

    # 2. Teste de Instanciação com dados INVÁLIDOS (Provando a validação no construtor)
    print("\n--- Teste 1: Tentativa de criar com média negativa ---")
    objeto_invalido = Aluno("João Souza", -3.0)
    print(f"Resultado mantido com segurança: Média {objeto_invalido.get_media():.2f}")

    # 3. Teste de alteração via Setter com dado INVÁLIDO
    print("\n--- Teste 2: Tentativa de alterar o nome para um texto muito curto ---")
    objeto_valido.set_nome("AB")
    print(f"Nome do objeto protegido: {objeto_valido.get_nome()}")  