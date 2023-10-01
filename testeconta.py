from abc import ABC,abstractclassmethod
from datetime import datetime

def formatarData(data):
    return data.strftime("%d/%m/%Y %H:%M:%S")

class Transacao:
    def __init__(self,conta,valor,descricao, nova_transacao = False):
        self.__conta = conta
        self.__valor = valor
        self.__descricao = descricao
        self.__data = formatarData(datetime.now())

        # conta.lista_transacoes.append(self)  
        
        if nova_transacao == False:
            if valor < 0:
                conta.retirada((-1) * valor, descricao, self)
  
            elif valor > 0:
                conta.deposito(valor, descricao, self)
                
    @property
    def data(self):
        return self.__data
        
    @property
    def conta(self):
        return self.__conta
    
    @property
    def valor(self):
        return self.__valor
    
    @property
    def descricao(self):
        return self.__descricao
    
    

class Conta(ABC):
    
    def __init__(self,nome,numero,saldo):
        self.__nome = nome
        self.__numero = numero
        self.__saldo = saldo
        self.__lista_transacoes = []
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def lista_transacoes(self):
        return self.__lista_transacoes
    
    @saldo.setter
    def saldo(self,saldo):
        self.__saldo = saldo   
        
    @lista_transacoes.setter
    def lista_transacoes(self,valor):
        self.__lista_transacoes = valor
        
    def retirada(self,valor,descricao, transacao = None):
        if valor <= self.__saldo and transacao is None:
            self.__saldo -= valor
            transacao = Transacao(self,-valor,descricao,True)
            self.lista_transacoes.append(transacao)
          
        elif valor <= self.__saldo and transacao is not None:
            self.__saldo -= valor
            self.lista_transacoes.append(transacao)
       
        else:
            print("Saldo Insuficiente")
            
    def deposito(self,valor,descricao, transacao = None):
        if  transacao is None:
            self.__saldo += valor
            transacao = Transacao(self,valor,descricao,True)
            
        elif transacao is not None:
            self.__saldo += valor
          

    @abstractclassmethod
    def imprimirExtrato(self):

        print()

class ContaComum(Conta):
    def __init__(self,nome,numero,saldo):
        super().__init__(nome,numero,saldo)
    
    def imprimirExtrato(self):
        print(f"Conta Comum:\nNome: {self.nome}  Número: {self.numero}  Saldo: {self.saldo}\n")
        if len(self.lista_transacoes) > 0:
            print("Transações: ")
            for i in self.lista_transacoes:
                sinal = "+" if i.valor > 0 else ""
                print(f"Data: {i.data} Valor: R$ {sinal}{i.valor} Descrição: {i.descricao}")
                print(" ")


class ContaPoupanca(Conta):
    
    def __init__(self,nome,numero,saldo):
        super().__init__(nome,numero,saldo)
        self.__aniversario = datetime.now().day

    @property
    def aniversario(self):
        return self.__aniversario
    
class ContaComLimite(Conta):
    
    def __init__(self,nome,numero,saldo,limite):
        super().__init__(nome,numero,saldo)
        self.__limite = limite
        self.__limite_inicial = limite
        
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self,novo_limite):
        self.__limite = novo_limite
        

    def retirada(self,valor,descricao, transacao = None):
        # ajuste do valor :
        valor = - valor if valor < 0 else valor
        if transacao is None:
   
            if self.saldo -valor >= 0:
                self.saldo -= valor
                transacao = Transacao(self,valor,descricao,True)
                self.lista_transacoes.append(transacao)

            elif self.saldo > 0 and self.saldo -valor  < 0  and self.__limite - (valor - self.saldo) >= 0:
                valor_restante = valor - self.saldo
                self.saldo -= valor 
                self.__limite -= valor_restante
                transacao = Transacao(self,valor,descricao,True)
                self.lista_transacoes.append(transacao)

            elif self.saldo < 0 and self.__limite > 0 and self.__limite < self.__limite_inicial and self.__limite - valor >= 0:
                self.saldo -= valor
                self.__limite -= valor
                transacao = Transacao(self,valor,descricao,True)
                self.lista_transacoes.append(transacao)         
        else:   

            if self.saldo -valor >= 0:
                self.saldo -= valor
                self.lista_transacoes.append(transacao)

            elif self.saldo > 0 and self.saldo -valor  < 0  and self.__limite - (valor - self.saldo) >= 0:
                valor_restante = valor - self.saldo
                self.saldo -= valor 
                self.__limite -= valor_restante
                self.lista_transacoes.append(transacao)

            elif self.saldo < 0 and self.__limite > 0 and self.__limite < self.__limite_inicial and self.__limite - valor >= 0:
                self.saldo -= valor
                self.__limite -= valor
                self.lista_transacoes.append(transacao)

           
            
    def deposito(self,valor,descricao, transacao = None):
        # ajuste do valor
        valor = -valor if valor < 0 else valor
        if transacao == None:
            
            if valor + self.__limite <= self.__limite_inicial:
                self.saldo += valor
                self.__limite += valor
                transacao = Transacao(self,valor,descricao,True)
                self.lista_transacoes.append(transacao)
             
            
            elif valor + self.__limite > self.__limite_inicial:
                self.__limite = self.__limite_inicial
                self.saldo += valor
                transacao = Transacao(self,valor,descricao,True)
                self.lista_transacoes.append(transacao)
               
        else:
            if valor + self.__limite <= self.__limite_inicial:
                self.saldo += valor
                self.__limite += valor
                self.lista_transacoes.append(transacao)
              
            elif valor + self.__limite > self.__limite_inicial:
                self.__limite = self.__limite_inicial
                self.saldo += valor
                self.lista_transacoes.append(transacao)            
              
                
    def imprimirExtrato(self):
        print(f"Conta Limite\nNome: {self.nome}  Número: {self.numero}  Saldo: {self.saldo}")
        print(f"Limite: {self.__limite}\n")
        if len(self.lista_transacoes) > 0:
            print("Transações: ")
            for i in self.lista_transacoes:
                sinal = "+" if i.valor > 0 else ""
                print(f"Data: {i.data} Valor: R$ {sinal}{i.valor} Descrição: {i.descricao}")
                print(" ")
    
if __name__ == "__main__":
    conta = ContaComLimite("Maria",123,1000,1000)
    conta.imprimirExtrato()
    trans = Transacao(conta,-800,"Retirada")
    trans = Transacao(conta,100,"Deposito")
    trans = Transacao(conta,-400,"Retirada")
    trans = Transacao(conta,-400,"Retirada")
    trans = Transacao(conta,-300,"Retirada")
    trans = Transacao(conta,-200,"Retirada")

    conta.imprimirExtrato()
