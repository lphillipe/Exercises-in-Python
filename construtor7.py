class Livro:
    def __init__(self, nome, autor):
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

    def buscar_por_autor(self, autor):
        encontrados = []
        for livro in self.livros:
            if livro.autor == autor:
                encontrados.append(livro)
        
        return encontrados


    def listar(self):
        for livro in self.livros:
            print(f"Nome do livro é {livro.nome} e seu autor é {livro.autor}")

l1 = Livro("Dom Casmurro", "Machado de Assis")
l2 = Livro("Memórias Póstumas", "Machado de Assis")
l3 = Livro("Capitães da Areia", "Jorge Amado")

bib = Biblioteca("Central")

bib.adicionar_livro(l1)
bib.adicionar_livro(l2)
bib.adicionar_livro(l3)

resultado = bib.buscar_por_autor("Machado de Assis")

for livro in resultado:
    print(livro.nome)