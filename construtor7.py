class Livro:
    def __init___(self, nome, autor):
        self.nome = nome
        self.autor = autor

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        if not isinstance(livro, Livro):
            print("Inválido não é um livro.")
            return False
        
        self.livros.append(livro)