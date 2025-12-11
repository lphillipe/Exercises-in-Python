class Senha:
    def __init__(self, nome, senha):
        if not isinstance(senha, str):
            raise TypeError("A Senha precisa ser uma string")

        self.nome = nome
        self.senha = senha

u = Senha("Ana", 123)