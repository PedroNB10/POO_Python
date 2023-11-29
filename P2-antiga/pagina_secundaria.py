# bibliotecas
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os.path
import pickle


class Peixe:
    def __init__(self, nome:str, preco:float):
        self.__nome = nome
        self.__preco = preco
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def preco(self):
        return self.__preco

class ConjuntoPeixes:
    def __init__(self, tipo_peixe, peso_total):
        self.__tipo_peixe = tipo_peixe
        self.__peso_total = peso_total
        
    @property
    def tipo_peixe(self):
        return self.__tipo_peixe
    
    @property
    def peso_total(self):
        return self.__peso_total
    

class Comanda:
    def __init__(self, numero:int, conjunto_peixes:list):
        self.__numero = numero
        self.__lista_de_peixes = conjunto_peixes
        self.__valor_total = 0
        
    @property
    def numero(self):
        return self.__numero
    
    @property
    def lista_de_peixes(self):
        return self.__lista_de_peixes
    
    
    @property
    def valor_total(self):
        return self.__valor_total
    
    @valor_total.setter
    def valor_total(self, valor_total):
        self.__valor_total = valor_total

        
    

    
    

class ModeloGenerico:
    def __init__(self, numero):
        self.numero = numero # .numero chama o setter para fazer a validação
            
    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero):
        try:
            numero = int(numero)
        except ValueError:
            raise ValueError("O número deve ser inteiro")
        
               
        try:
            if numero < 1:
                raise ValueError(f"O número {numero} deve ser maior que 0")
            
        except ValueError as error:
            raise ValueError(str(error))
        
        self.__numero = numero
        
        
class FechamentoComandaView(tk.Toplevel):
    def __init__(self, controle):
        self.controle = controle
        tk.Toplevel.__init__(self)
        
        self.root_height = 300
        self.root_width = 300
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        x_cordinate = int((self.screen_width/2) - (self.root_width/2))
        y_cordinate = int((self.screen_height/2) - (self.root_height/2))
        self.title("Fechamento Comanda")   
        self.geometry("{}x{}+{}+{}".format(self.root_width, self.root_height, x_cordinate, y_cordinate))
        
        self.frame_01 = tk.Frame(self)
        self.frame_01.pack()

        self.label_01 = tk.Label(self.frame_01, text="Peixes Disponíveis")
        self.label_01.pack(side="left")
        
    
        self.combo_box_peixes = ttk.Combobox(self.frame_01)
        self.combo_box_peixes['values'] = [peixe.nome for peixe in  self.controle.lista_de_peixes]
        self.combo_box_peixes.pack()
        

        
        self.frame_02 = tk.Frame(self)
        self.frame_02.pack()
        
        self.label_02 = tk.Label(self.frame_02, text="Peso dos peixes:")
        self.label_02.pack(side="left")

        self.entry_peso_peixe = tk.Entry(self.frame_02)
        self.entry_peso_peixe.pack()

        self.button_adicionar_peixe = tk.Button(self, text="Adicionar Peixe", command=self.controle.adicionar_peixe_comanda)
        self.button_adicionar_peixe.pack(pady=20)
        
        self.button_fechar_comanda = tk.Button(self, text="Fechar Comanda", command=self.controle.fechar_comanda)
        self.button_fechar_comanda.pack(pady=20)

        
        self.button_fechar = tk.Button(self, text="Fechar", command=lambda:self.controle.fechar_tela(self))
        self.button_fechar.pack(pady=20)
    
    


    
class CadastroPeixeView(tk.Toplevel):
    def __init__(self, controle):
        self.controle = controle
        tk.Toplevel.__init__(self)
        
        self.root_height = 300
        self.root_width = 300
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        x_cordinate = int((self.screen_width/2) - (self.root_width/2))
        y_cordinate = int((self.screen_height/2) - (self.root_height/2))
        self.title("Cadastro Peixe")   
        self.geometry("{}x{}+{}+{}".format(self.root_width, self.root_height, x_cordinate, y_cordinate))
        
        self.frame_01 = tk.Frame(self)
        self.frame_01.pack()

        self.label_01 = tk.Label(self.frame_01, text="Nome do Peixe")
        self.label_01.pack(side="left")

        self.entry_nome_peixe = tk.Entry(self.frame_01)
        self.entry_nome_peixe.pack()
        
        self.frame_02 = tk.Frame(self)
        self.frame_02.pack()
        
        self.label_02 = tk.Label(self.frame_02, text="Preço do Peixe")
        self.label_02.pack(side="left")
        
        self.entry_preco_peixe = tk.Entry(self.frame_02)
        self.entry_preco_peixe.pack()
        
        
        self.button_cadastrar = tk.Button(self, text="Cadastrar", command=self.controle.cadastrar_peixe)
        self.button_cadastrar.pack(pady=20)

        
        self.button_fechar = tk.Button(self, text="Fechar", command=lambda:self.controle.fechar_tela(self))
        self.button_fechar.pack(pady=20)


class JanelaSecondaria(tk.Toplevel):
    def __init__(self, controle):
        self.controle = controle
        tk.Toplevel.__init__(self)
        
        self.root_height = 300
        self.root_width = 300
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        x_cordinate = int((self.screen_width/2) - (self.root_width/2))
        y_cordinate = int((self.screen_height/2) - (self.root_height/2))
        self.title("Janela Secondária")   
        self.geometry("{}x{}+{}+{}".format(self.root_width, self.root_height, x_cordinate, y_cordinate))
        
        
        self.frame_01 = tk.Frame(self)
        self.frame_01.pack()

        self.label_01 = tk.Label(self.frame_01, text="Label 01")
        self.label_01.pack(side="left")

        self.entry_01 = tk.Entry(self.frame_01)
        self.entry_01.pack()

        self.button_01 = tk.Button(self, text="Cadastrar Instancias", command=self.controle.cadastrar_instancias) 
        self.button_01.pack(pady=20)
        
        self.button_02 = tk.Button(self, text="Mostrar Instancias", command=self.controle.mostrar_instancias)
        self.button_02.pack(pady=20)
        
        self.button_03 = tk.Button(self, text="Salvar Instancias", command=self.controle.salvar_instancias)
        self.button_03.pack(pady=20)
        
        self.button_fechar = tk.Button(self, text="Fechar", command=lambda:self.controle.fechar_tela(self))
        self.button_fechar.pack(pady=20)
        

class ControleSecundario:
    def __init__(self, controle_principal):
        self.controle_principal = controle_principal
        
        self.lista_de_peixes = []
        self.lista_de_comandas = []
        
        self.lista_temp_peixes = []


        
        if not os.path.isfile("instancia.pickle"):
            self.lista_de_classes = []
            
        else:
            with open("instancia.pickle", "rb") as f:
                self.lista_de_classes = pickle.load(f)
        
    def salvar_instancias(self):
        if len(self.lista_de_classes) != 0:
            with open("instancia.pickle","wb") as f:
                pickle.dump(self.lista_de_classes, f)
                
                
        print("Instancias salvas")
        
        
    def mostrar_fatura(self):
        print("mostrar fatura")
        if len(self.lista_de_comandas) == 0:
                messagebox.showinfo("Faturamento", "Não há comandas cadastradas")
                return
            
        str = ""
        str += "------------\n"
        total = 0
        for peixe in self.lista_de_peixes:
            total_peso_acumulado = 0
            total_arrecadado = 0
            
            for comanda in self.lista_de_comandas:
                for conjunto_peixes in comanda.lista_de_peixes:
                    if peixe.nome == conjunto_peixes.tipo_peixe:
                        total_peso_acumulado += conjunto_peixes.peso_total
                        total_arrecadado += conjunto_peixes.peso_total * peixe.preco
            
            total += total_arrecadado
            str += f"Nome do peixe: {peixe.nome}\n"
            str += f"Total de peso acumulado: {total_peso_acumulado}\n"
            str += f"Total arrecadado: {total_arrecadado}\n"
            str += "------------------------\n"
            
            
        str += f"Total: {total}\n"
            
        messagebox.showinfo("Faturamento", str)
        
    def retornar_instancia_peixe(self, nome_peixe):
        for peixe in self.lista_de_peixes:
            if peixe.nome == nome_peixe:
                return peixe
            
        return None
        
    def adicionar_peixe_comanda(self):
        print("adicionar peixe comanda")
        tipo_peixe = self.view_fechar_comanda.combo_box_peixes.get()
        peso = self.view_fechar_comanda.entry_peso_peixe.get()
        peso = float(peso)
        self.lista_temp_peixes.append(ConjuntoPeixes(tipo_peixe, peso))
        messagebox.showinfo("Alerta", "Peixe adicionado com sucesso")
        
        
    def fechar_comanda(self):
        print("fechar comanda")
        numero_comanda = len(self.lista_de_comandas) + 1
        comanda = Comanda(numero_comanda, self.lista_temp_peixes)
        
        for conjunto_peixes in comanda.lista_de_peixes:
            nome_peixe =  conjunto_peixes.tipo_peixe
           
            peixe_objeto = self.retornar_instancia_peixe(nome_peixe)
            
            peso_total =(conjunto_peixes.peso_total)  # Ensure peso_total is a numeric value
            comanda.valor_total += peso_total * peixe_objeto.preco
        
        self.lista_de_comandas.append(comanda)
        messagebox.showinfo("Alerta", "Comanda fechada com sucesso")
        str = ""
        str += f"Comanda número: {comanda.numero}\n"
        str += f"Valor total: {comanda.valor_total}\n"
        str += "Peixes:\n"
        for conjunto_peixes in comanda.lista_de_peixes:
            str += f"Tipo do peixe: {conjunto_peixes.tipo_peixe}\n"
            str += f"Peso total: {conjunto_peixes.peso_total}\n"

            
        messagebox.showinfo("Comanda", str)
        print(self.lista_de_comandas)
        
        

    def cadastrar_peixe(self):
        nome = self.view_cadastro_peixe.entry_nome_peixe.get()
        preco = self.view_cadastro_peixe.entry_preco_peixe.get()
        

        try:
            preco = float(preco)
            peixe = Peixe(nome, preco)
            self.lista_de_peixes.append(peixe)
            messagebox.showinfo("Alerta", "Peixe cadastrado com sucesso")
            print(self.lista_de_peixes)
            
            
        except ValueError as error:
            messagebox.showinfo("Alerta", str(error))
            return
    
    def cadastrar_instancias(self):
        
        print("cadastrar instancias")
        try:
            modelo_01 = ModeloGenerico(1)
            self.lista_de_classes.append(modelo_01)
            modelo_02 = ModeloGenerico(2)
            self.lista_de_classes.append(modelo_02)
            modelo_03 = ModeloGenerico(6)
            self.lista_de_classes.append(modelo_03)
            modelo_04 = ModeloGenerico(4)
            self.lista_de_classes.append(modelo_04)
            modelo_05 = ModeloGenerico(5)
            self.lista_de_classes.append(modelo_05)
        
            
            
        except ValueError as error:
            messagebox.showinfo("Alerta", str(error))
            return
        
        
        
    def mostrar_instancias(self):
        if len(self.lista_de_classes) == 0:
            print("Não há instancias cadastradas")
        
        str = ''
        str += "Instancias cadastradas:\n"
        str += "-----------------------\n"
    
        for modelo in self.lista_de_classes:
            str += f"Classe Modelo : {modelo.numero}\n"
            
        messagebox.showinfo("Instancias", str)
            
            
    def criar_tela_fechar_comanda(self):
        self.lista_temp_peixes = []
        self.view_fechar_comanda = FechamentoComandaView(self)
            
    def criar_tela_cadastro_peixe(self):  
        self.view_cadastro_peixe = CadastroPeixeView(self)        

    
    def criar_tela_secundaria(self):
        self.view_secundaria = JanelaSecondaria(self)
        
            
        
    def fechar_tela(self, janela):
        janela.destroy()

        
        