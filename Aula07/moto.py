class moto:
    
    # construtor
    def __init__(self, marca, cor, motor_ligado):
        self.__marca = marca
        self.__cor = cor
        self.__motor_ligado = motor_ligado

    # método de instância
    def ligaMotor(self):
        if self.__motor_ligado == True:
            print('O motor já está ligado!')
        else:
            self.__motor_ligado = True
            print('O motor acaba de ser ligado!')
    def MostraProdutos(self):
        
        print(f"Essa é uma {self.__marca} de cor {self.__cor}.")
        
        if self.__motor_ligado == True:
            print("Seu motor está ligado! ")
        else:
            print("Seu motor está desligado! ")

moto1 = moto(cor="vermelha", marca="Toyota",motor_ligado=False)
moto1.MostraProdutos()

print()
moto1.ligaMotor()

print()
moto1.MostraProdutos()
print()
moto2 = moto("Honda", "vermelha",True)
moto2.MostraProdutos()