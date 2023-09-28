from abc import ABC,abstractclassmethod

class Conta(ABC):
    
    def __init__(self,numero, nome, saldo):
        self.__numero = numero
        self.__nome = nome
        self.__saldo = saldo
        
        self.__lista_transacoes = []

    @property
    def numero(self):
        return self.__numero
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def lista_transacoes(self):
        return self.__lista_transacoes
    
    
    def adicionarTransacao(self,transacao):
        
        self.__lista_transacoes.append(transacao)
    
    
    # @abstractclassmethod
    # def imprimirExtrato(self):
    #     pass
    
    
class ContaPoupanca(Conta):
    def __init__(self,numero,nome,conta,aniversario):
        super().__init__(numero,nome,conta)
        self.__aniversario = aniversario
        
    @property
    def aniversario(self):
        return self.__aniversario
    

class ContaCorrenteComum(Conta):
    def __init__(self,numero,nome,conta):
        super().__init__(numero,nome,conta)
        

class ContaLimite(Conta):
    def __init__(self,numero,nome,conta, valorLimite):
        super().__init__(numero,nome,conta)
        self.__valorLimite = valorLimite
        
    @property
    def valorLimite(self):
        return self.__valorLimite



class Transacao():
    def __init__(self, conta, data, valor, descricao):
        self.__conta = conta
        self.__data = data
        self.__valor = valor
        self.__descricao = descricao
        conta.adicionarTransacao(self) # ao criar transacao ela ja é adicionada a lista de transações na classe conta
    
    @property
    def conta(self):
        self.__conta
    
    @property
    def data(self):
        return self.__data
    
    @property
    def valor(self):
        return self.__valor
    
    @property
    def descricao(self):
        return self.__descricao
    
    
    
    
if __name__ ==  "__main__":
    #criando contas
    conta1 = ContaPoupanca(1,"Joao",1000,"10/10/2020")
    transacao1 = Transacao(conta1,"10/10/2020",200,"Deposito")
    
    print(conta1.nome)
    print(conta1.lista_transacoes[0].valor)
    