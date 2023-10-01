from abc import ABC,abstractclassmethod
from datetime import datetime
import random

def formatarData(data):
    return data.strftime("%d/%m/%Y %H:%M:%S")

class Transacao:
    def __init__(self,conta,valor, nova_transacao = False):
        self.__conta = conta
        self.__valor = valor
        self.__descricao = "Crédito" if valor > 0 else "Débito"
        self.__data = formatarData(datetime.now())

        if nova_transacao == False:
            if valor < 0:
                conta.retirada((-1) * valor, self)
  
            elif valor > 0:
                conta.deposito(valor, self)
                
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
    
    def __init__(self,nome):
        self.__nome = nome
        self.__numero = str(random.randint(10**12, 10**13 - 1))
        self.__saldo = 0
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
        
    def retirada(self,valor,transacao = None):
        if valor < 0:
            print("Valor Inválido")
        
        elif self.saldo - valor < 0:
            print("Saldo Insuficiente!")

        else:
            if valor <= self.__saldo and transacao is None:
                self.__saldo -= valor
                transacao = Transacao(self,-valor,True)
                self.lista_transacoes.append(transacao)
            
            elif valor <= self.__saldo and transacao is not None:
                self.__saldo -= valor
                self.lista_transacoes.append(transacao)
        
            else:
                print("Saldo Insuficiente")
            
    def deposito(self,valor,transacao = None):
        if valor < 0:
            print("Valor Inválido")
        else:
            if  transacao is None:
                self.__saldo += valor
                transacao = Transacao(self,valor,True)
                self.lista_transacoes.append(transacao)
            elif transacao is not None:
                self.__saldo += valor
                self.lista_transacoes.append(transacao)

    @abstractclassmethod
    def imprimirExtrato(self):
        pass

class ContaComum(Conta):
    def __init__(self,nome):
        super().__init__(nome)
    
    def imprimirExtrato(self):
        print(f"Conta Corrente Comum:\nNome: {self.nome}  Número: {self.numero}  Saldo: {self.saldo}\n")
        if len(self.lista_transacoes) > 0:
            print("Transações: ")
            for i in self.lista_transacoes:
                sinal = "+" if i.valor > 0 else ""
                print(f"\tData: {i.data} Valor: R$ {sinal}{i.valor} Descrição: {i.descricao}")



class ContaPoupanca(Conta):
    
    def __init__(self,nome):
        super().__init__(nome)
        # para pegar o dia de criacao => formatarData(datetime.now())
        self.__aniversario = datetime.now().day

    @property
    def aniversario(self):
        return self.__aniversario
    
    def imprimirExtrato(self):
        print(f"Conta Poupança:\nNome: {self.nome}  Número: {self.numero}  Saldo: {self.saldo} Dia do Aniversário: {self.__aniversario}\n")
        if len(self.lista_transacoes) > 0:
            print("Transações: ")
            for i in self.lista_transacoes:
                sinal = "+" if i.valor > 0 else ""
                print(f"\tData: {i.data} Valor: R$ {sinal}{i.valor} Descrição: {i.descricao}")
    
class ContaComLimite(Conta):
    
    def __init__(self,nome,limite):
        super().__init__(nome)
        self.__limite = limite
        self.__limite_inicial = limite
        
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self,novo_limite):
        self.__limite = novo_limite
        

    def retirada(self,valor, transacao = None):
        if valor < 0:
            print("Valor Inválido")

        else:
            if transacao is None:
    
                if self.saldo -valor >= 0:
                    self.saldo -= valor
                    transacao = Transacao(self,valor,True)
                    self.lista_transacoes.append(transacao)

                elif self.saldo > 0 and self.saldo -valor  < 0  and self.__limite - (valor - self.saldo) >= 0:
                    valor_restante = valor - self.saldo
                    self.saldo -= valor 
                    self.__limite -= valor_restante
                    transacao = Transacao(self,valor,True)
                    self.lista_transacoes.append(transacao)

                elif self.saldo < 0 and self.__limite > 0 and self.__limite < self.__limite_inicial and self.__limite - valor >= 0:
                    self.saldo -= valor
                    self.__limite -= valor
                    transacao = Transacao(self,valor,True)
                    self.lista_transacoes.append(transacao)  
                else:
                    print("Saldo Insuficiente")       
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
                
                else:
                    print("Saldo Insuficiente")

    def deposito(self,valor,transacao = None):
        if valor < 0:
            print("Valor Inválido")
        else:
            if transacao == None:
                
                if valor + self.__limite <= self.__limite_inicial:
                    self.saldo += valor
                    self.__limite += valor
                    transacao = Transacao(self,valor,True)
                    self.lista_transacoes.append(transacao)
                
                
                elif valor + self.__limite > self.__limite_inicial:
                    self.__limite = self.__limite_inicial
                    self.saldo += valor
                    transacao = Transacao(self,valor,True)
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
        print(f"Conta Corrente com Limite\nNome: {self.nome}  Número: {self.numero}  Saldo: {self.saldo} Limite: {self.__limite}\n")
        if len(self.lista_transacoes) > 0:
            print("Transações: ")
            for i in self.lista_transacoes:
                sinal = "+" if i.valor > 0 else ""
                print(f"\tData: {i.data} Valor: R$ {sinal}{i.valor} Descrição: {i.descricao}")

    
if __name__ == "__main__":
    conta = ContaComLimite("Maria",1500)
    conta2 = ContaPoupanca("Bob")
    conta3 = ContaComum("Joel")
    conta.imprimirExtrato()
    # conta2.imprimirExtrato()
    # conta3.imprimirExtrato()
    conta.deposito(1000)

    trans = Transacao(conta,-800)
    trans = Transacao(conta,-400)
    trans = Transacao(conta,-400)
    trans = Transacao(conta,-300)
    trans = Transacao(conta,-200)
    trans = Transacao(conta,-400)
    trans = Transacao(conta,-1)
    conta.imprimirExtrato()