class Senha:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

        if not isinstance(senha, str):
            raise TypeError("A senha precisa ser uma string.")

u = Senha("Ana", 123)