class Veiculo:
    def __init__(self, marca, cor, motor_ligado):
        self.__marca = marca
        self.__cor = cor
        self.__motor_ligado = motor_ligado
    
    def ligar_motor(self):
        
        if self.__motor_ligado == True:
            print("O motor está já está ligado")
        else:
            print("Motor ligado!")
            self.estado_porta_malas = True
        
    def mostraArtibutos(self):
        print(f"""Marca: {self.__marca}
Cor: {self.__cor}
Motor está {"Ligado" if self.__motor_ligado else "Desligado" }
""", end="")

        

        
    
class Moto(Veiculo):
    def __init__(self, marca, cor, motor_ligado=False, estilo="custom"): # coloquei parâmetro como false para se comportar como default, caso o usuário não coloque os estados do motor e o estilo
        super().__init__(marca, cor, motor_ligado)
        self.__estilo = estilo
        
    @property
    def estilo(self):
       return self.__estilo 
    def mostraArtibutos(self):
        super().mostraArtibutos()
        print(f"""Estilo: {self.__estilo} \n""")


    
class Carro(Veiculo):
    def __init__(self, marca, cor, motor_ligado= False, estado_porta_malas=False):
        super().__init__(marca, cor, motor_ligado)
        self.__estado_porta_malas = estado_porta_malas
        
    @property
    def __motor_ligado(self):
        return self.__motor_ligado 
        
    @property
    def estado_porta_malas(self):
        return self.__estado_porta_malas 
    
    def abrir_porta_malas(self):
        
        if self.estado_porta_malas == True:
            print("Porta malas já está aberto")
        else:
            self.__estado_porta_malas = True
    
    
    def mostraArtibutos(self):
        super().mostraArtibutos()
        print(f"""Porta malas {"aberto "if self.estado_porta_malas else "fechado" } \n""")

        

        


carro = Carro("Ford", "preto")
moto = Moto("Honda", "rosa", estilo="esportiva")

novaMoto = Moto("Yamaha", "vermelha")

novaMoto.mostraArtibutos()
moto.mostraArtibutos()
carro.mostraArtibutos()

carro.abrir_porta_malas()
carro.mostraArtibutos()