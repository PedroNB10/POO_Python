class Animal:
    
    def __init__(self, nome):
        self.__nome = nome
        
    @property
    def nome(self):
        return self.__nome
    
    def fazerCarinho(self):
        print(f"{self.__nome} está recebendo carinho.")
    
# classe gato é subclasse da classe animal
class Gato(Animal):
    
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.__raca = raca
        
    # precisa usar property porque é uma variavel única de gato
    @property
    def raca(self):
        return self.__raca

    # método de instância
    def miar(self):
        print("MEEEEEEOOOOOOOOOOOOOOW")
        
class Cao(Animal):
    
    def __init__(self, nome):
        super().__init__(nome)

    # método de instância
    def latir(self):
        print("AU AU AU AU AU AU AU AU AU AU AU")
    


if __name__ == "__main__":
    gato = Gato('Leon', 'Preto')
    print(gato.nome)
    print(gato.raca)
    gato.miar()
    gato.fazerCarinho()
    

