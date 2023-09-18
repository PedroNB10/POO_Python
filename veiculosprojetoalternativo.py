class Veiculo:
    def __init__(self, marca, cor, motor_ligado):
        self.marca = marca
        self.cor = cor
        self.motor_ligado = motor_ligado
    
    def ligar_motor(self):
        if self.motor_ligado:
            print("O motor já está ligado")
        else:
            print("Motor ligado!")
            self.motor_ligado = True




class Moto(Veiculo):
    def __init__(self, marca, cor, motor_ligado=False, estilo="custom"):
        super().__init__(marca, cor, motor_ligado)
        self.estilo = estilo

    def mostraAtributos(self):
        print(f"""Marca: {self.marca}
Cor: {self.cor}
Motor está {"Ligado" if self.motor_ligado else "Desligado" }""")
        print(f"Estilo: {self.estilo}\n")


class Carro(Veiculo):
    def __init__(self, marca, cor, motor_ligado=False, estado_porta_malas=False):
        super().__init__(marca, cor, motor_ligado)
        self.estado_porta_malas = estado_porta_malas

    def abrir_porta_malas(self):
        if not self.estado_porta_malas:
            print("Porta malas aberto")
            self.estado_porta_malas = True
        else:
            print("Porta malas já está aberto")
    
    def mostraAtributos(self):
        print(f"""Marca: {self.marca}
Cor: {self.cor}
Motor está {"Ligado" if self.motor_ligado else "Desligado" }""")
        print(f"Porta malas {'aberto' if self.estado_porta_malas else 'fechado'}\n")


carro = Carro("Ford", "preto")
moto = Moto(marca="Honda", cor="rosa")

novaMoto = Moto("Yamaha", cor="vermelha")

moto.mostraAtributos()
carro.mostraAtributos()
novaMoto.mostraAtributos()
