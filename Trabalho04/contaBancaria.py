from abc import ABC,abstractclassmethod
from datetime import datetime

def formatarData(data):
    return data.strftime("%d/%m/%Y %H:%M:%S")
            
class Conta(ABC):
    
    def __init__(self,numero, nome, saldo): # sugestao use parametros pre criados para lista_transicoes e nao precisar acessar _Conta__lista_de_transicoes
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
    
   # Método Privado
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
    
    @property
    def lista_transacoes(self):
        return self.__lista_transacoes
    
    def Deposito(self,valor,descricao,transacao = None):
        self.__saldo += valor 
        if transacao is None:
            transacao = Transacao(self,valor,descricao,False)

    def Retirada(self,valor,descricao, transacao = None, saldo_ultrapassado = False):
        
        if valor <= self.__saldo:
            self.__saldo -= valor 
            if transacao is None:
                transacao = Transacao(self,-valor,descricao,False)
        elif saldo_ultrapassado == True and transacao is None and valor > self.__saldo:
            self.__saldo -= valor
            transacao = Transacao(self,-valor,descricao,False)
            
        else:
            print("Valor acima do saldo!")
            
    @abstractclassmethod
    def imprimirExtrato(self):
        pass
    
    
class ContaPoupanca(Conta):
    def __init__(self,numero,nome,saldo):
        super().__init__(numero,nome,saldo)
        self.__aniversario = datetime.now().day
        
    @property
    def aniversario(self):
        return self.__aniversario
    

    def imprimirExtrato(self):
        print("Conta Poupança")
        print("Nome: ", self.nome)
        print("Numero: ", self.numero)
        print("Saldo: ", self.saldo)
        print("Aniversario: ", self.aniversario)
        if len(self.lista_transacoes) > 0:
            print("Transações: ")
            for i in self.lista_transacoes:
                sinal = "+" if i.valor > 0 else ""
                print(f"Data: {i.data} Valor: R$ {sinal}{i.valor} Descrição: {i.descricao}")
                print(" ")
    print()

class ContaCorrenteComum(Conta):
    def __init__(self,numero,nome,saldo):
        super().__init__(numero,nome,saldo)

    def imprimirExtrato(self):
        print("Conta Comum")
        print("Nome: ", self.nome)
        print("Numero: ", self.numero)
        print("Saldo: ", self.saldo)
        if len(self.lista_transacoes) > 0:
            print("Transações: ")
            for i in self.lista_transacoes:
                sinal = "+" if i.valor > 0 else ""
                print(f"Data: {i.data} Valor: R$ {sinal}{i.valor} Descrição: {i.descricao}")
                print(" ")
    print()

class ContaLimite(Conta):
    def __init__(self,numero,nome,saldo, valorLimite):
        super().__init__(numero,nome,saldo)
        self.__valorLimite = valorLimite
        self.__valorLimiteInicial = valorLimite
    
        

    @property
    def valorLimite(self):
        return self.__valorLimite

    def Retirada(self,valor,descricao):
        if valor > self.saldo and self.saldo >0 and valor - self.saldo <= self.__valorLimite:
                    
            super().Retirada(valor,descricao,None,True)
            
            self.__valorLimite = self.__valorLimite -  (-1)* self.saldo
        elif self.saldo < 0 and self.__valorLimite > 0 and valor <= self.__valorLimite:
             super().Retirada(valor,descricao,None,True)
             self.__valorLimite -= valor
            
        elif self.saldo == 0 and self.__valorLimite > 0:
            super().Retirada(valor,descricao,None,True)
            self.__valorLimite -= valor
        elif valor <= self.saldo:
            super().Retirada(valor,descricao)
        
        else:
            print("Valor acima do limite!")
    
    def Deposito(self,valor,descricao,transacao = None):
        if self.saldo >= 0 and self.__valorLimite == self.__valorLimiteInicial:
            super().Deposito(valor,descricao)
        elif self.saldo < 0 and self.__valorLimite > 0:

            if self.__valorLimite + valor <= self.__valorLimiteInicial:
                
                super().Deposito(valor,descricao,transacao)
                self.__valorLimite += valor
                     
     

        
    def imprimirExtrato(self):
        print("Conta Limite")
        print("Nome: ", self.nome)
        print("Numero: ", self.numero)
        print("Saldo: ", self.saldo)
        print("Valor Limite: ", self.valorLimite)
        if len(self.lista_transacoes) > 0:
            print("Transações: ")
            for i in self.lista_transacoes:
                sinal = "+" if i.valor > 0 else ""
                print(f"Data: {i.data} Valor: R$ {sinal}{i.valor} Descrição: {i.descricao}")
                print(" ")
            
        print()
class Transacao():
    def __init__(self, conta, valor, descricao, novaTransacao = True):
        self.__conta = conta
        self.__data = formatarData(datetime.now())
        self.__valor = valor
        self.__descricao = descricao
        conta.lista_transacoes.append(self)  
        if novaTransacao == True:
            if valor > 0:
                conta.Deposito(valor,descricao,self) # chama o metodo deposito da classe conta
            else:
                conta.Retirada(-1*valor,descricao,self)
    @property
    def conta(self):
        return self.__conta
    
    @property
    def data(self):
        return self.__data
    
    @property
    def valor(self):
        return self.__valor
    
    @property
    def descricao(self):
        return self.__descricao
    
    
        
    
if __name__ == "__main__":
    # Criando instâncias das contas
    conta_limite = ContaLimite(1, "João", 1000, 1000)
    conta_limite.imprimirExtrato()
    conta_limite.Retirada(500,"Retirada")   
    conta_limite.Retirada(600,"Retirada") 
    conta_limite.Retirada(700,"Retirada") 
    conta_limite.Deposito(800,"Deposito")
    conta_limite.Deposito(800,"Deposito")
    conta_limite.Deposito(400,"Deposito")
    conta_limite.imprimirExtrato()