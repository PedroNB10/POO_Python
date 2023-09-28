class Conta:
    def __init__(self): # Construtor = cria os atributos
        print("Construtor chamado")
        self.numero = 123
        self.titular = "João"
        self.saldo = 55.0
        self.limite = 1000.0