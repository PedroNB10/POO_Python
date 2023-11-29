# bibliotecas
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os.path
import pickle

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
            
            
            
            

    
    def criar_tela_secundaria(self):
        self.view_secundaria = JanelaSecondaria(self)
        
            
        
    def fechar_tela(self, janela):
        janela.destroy()

        
        