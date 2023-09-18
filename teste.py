class Veiculo:
    def __init__(self, marca, cor, motor_ligado):
        self._marca = marca
        self._cor = cor
        self._motor_ligado = motor_ligado
    
    def ligar_motor(self):
        if self._motor_ligado:
            print("O motor já está ligado")
        else:
            print("Motor ligado!")
            self._motor_ligado = True


class Moto(Veiculo):
    def __init__(self, marca, cor, motor_ligado=False, estilo="custom"):
        super().__init__(marca, cor, motor_ligado)
        self.__estilo = estilo  # Você pode manter '__' para estilo se quiser que ele seja privado
        
    def mostrar_atributos_moto(self):
        print(f"""Marca: {self._marca}
Cor: {self._cor}
Motor está {"Ligado" if self._motor_ligado else "Desligado"}\n""")
        print(f"Estilo: {self.__estilo}")


class Carro(Veiculo):
    def __init__(self, marca, cor, motor_ligado=False, estado_porta_malas=False):
        super().__init__(marca, cor, motor_ligado)
        self.__estado_porta_malas = estado_porta_malas
        
    def abrir_porta_malas(self):
        if not self.__estado_porta_malas:
            print("Porta malas aberto")
            self.__estado_porta_malas = True
        else:
            print("Porta malas já está aberto")
    
    def mostrar_atributos_carro(self):
        print(f"""Marca: {self._marca}
Cor: {self._cor}
Motor está {"Ligado" if self._motor_ligado else "Desligado"}""")
        print(f"Porta malas {'aberto' if self.__estado_porta_malas else 'fechado'}\n")
        

carro = Carro("Ford", "preto")
moto = Moto(marca="Honda", cor="rosa")

novaMoto = Moto("Yamaha", cor="vermelha")

moto.mostrar_atributos_moto()
carro.mostrar_atributos_carro()
carro.abrir_porta_malas()
carro.abrir_porta_malas()
