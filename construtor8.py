class Personagem:
    def __init__(self, nome, classe, vida=100, mana=50):
        self.nome = nome
        self.classe = classe
        self.vida = vida
        self.mana = mana

    def status(self):
        print("==== STATUS ====")
        print(f"Nome: {self.nome}")
        print(f"Classe: {self.classe}")
        print(f"Vida: {self.vida}")
        print(f"Mana: {self.mana}")
        print("================")


p1 = Personagem("AmericanO", "Blade Knight", 32767, 32767)
p2 = Personagem("StyleFox", "Mago", 80, 1000)
p3 = Personagem("Darkness", "Merlin")

p1.status()
p2.status()
p3.status()
