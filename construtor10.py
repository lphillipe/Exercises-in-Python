class Senha:
    def __init__(self, nome, senha):
        if not isinstance(senha, str):
            raise TypeError("A Senha precisa ser uma string")

        if len(senha) < 6:
            raise ValueError("A senha deve ter pelo menos 6 caracteres")

        self.nome = nome
        self.senha = senha

    def autenticar(self, senha_digitada):
        senha_digitada == self.senha



u = Senha("Ana", "123456")

print(u.autenticar("123456"))
print(u.autenticar("errada"))