class Veiculo:
    def __init__(self, marca, cor, motor_ligado):
        self.__marca = marca
        self.__cor = cor
        self.__motor_ligado = motor_ligado
    
    def mostraArtibutos(self):
        print(f"""
              Marca: {self.__marca}
              Cor: {self.__cor}
              Motor está {"Ligado" if self.__motor_ligado else "Desligado" }
              """)
        
        
        
    
class Moto(Veiculo):
    def __init__(self, marca, cor, motor_ligado, estilo):
        super().__init__(marca, cor, motor_ligado)
        self.__estilo = estilo
        
    @property
    def estilo(self):
       return self.__estilo 
    
class Carro(Veiculo):
    def __init__(self, marca, cor, motor_ligado, estado_porta_malas):
        super().__init__(marca, cor, motor_ligado)
        self.__estado_porta_malas = estado_porta_malas
        
    @property
    def __motor_ligado(self):
        return self.__motor_ligado 
        
    @property
    def estado_porta_malas(self):
        return self.__estado_porta_malas 


carro = Carro("Ford", "preto", True, False)
moto = Moto("Honda", "rosa", True, "custom")
moto.mostraArtibutos()
carro.mostraArtibutos()