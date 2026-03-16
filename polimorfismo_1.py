class Animal:

    def emitir_som(self):
        print('Qualquer som...')

class Cachorro(Animal):
    
    def emitir_som(self):
        print('Au Au!')

cachorro= Cachorro()
cachorro.emitir_som()