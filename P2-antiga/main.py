# bibliotecas
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os.path
import pickle

import pagina_secundaria


# Peixe -> Cadastrar, Mostra
# Comanda -> Fechamento
# Relatório -> Faturamento

class AuxiliarView(tk.Toplevel):
    def __init__(self, controle):
        self.controle = controle
        tk.Toplevel.__init__(self)
        
        self.root_height = 300
        self.root_width = 300
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        x_cordinate = int((self.screen_width/2) - (self.root_width/2))
        y_cordinate = int((self.screen_height/2) - (self.root_height/2))
        self.title("Tela Auxiliar")   
        self.geometry("{}x{}+{}+{}".format(self.root_width, self.root_height, x_cordinate, y_cordinate))
        
        
        self.frame_01 = tk.Frame(self)
        self.frame_01.pack()

        self.label_01 = tk.Label(self.frame_01, text="Label 01")
        self.label_01.pack(side="left")

        self.entry_01 = tk.Entry(self.frame_01)
        self.entry_01.pack()

        self.button_01 = tk.Button(self, text="Botão Auxiliar", command="") 
        self.button_01.pack(pady=20)


class MainView:
    def __init__(self, root,controle_principal):
        self.root = root
        self.controle_principal = controle_principal   
 
        self.root_height = 400
        self.root_width = 400
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        x_cordinate = int((self.screen_width/2) - (self.root_width/2))
        y_cordinate = int((self.screen_height/2) - (self.root_height/2))
        self.root.title("Tela Principal")   
        self.root.geometry("{}x{}+{}+{}".format(self.root_width, self.root_height, x_cordinate, y_cordinate))

        # colocar a inferface da tela aqui

        # criando os botoes do menu
        self.menu_bar = tk.Menu(self.root)
        self.sub_menu_01 = tk.Menu(self.menu_bar)
        self.sub_menu_02 = tk.Menu(self.menu_bar)
        self.sub_menu_03 = tk.Menu(self.menu_bar)
        self.botao_sair = tk.Menu(self.menu_bar)


        # menus tipos cascade tem outros menus dentro deles enquanto os menus tipo command são apenas botões, por isso os command não tem o atributo sub_menu

        self.menu_bar.add_cascade(label="Peixe", menu=self.sub_menu_01) # sub_menu
        self.menu_bar.add_cascade(label="Comanda", menu=self.sub_menu_02) # sub_menu
        self.menu_bar.add_cascade(label="Relatório", menu=self.sub_menu_03) # sub_menu
        self.menu_bar.add_command(label="Janela Secondaria", command=self.controle_principal.criar_janela_secundaria)
        self.menu_bar.add_command(label="Sair", command= self.controle_principal.fechar_janela_principal) # botão para sair, não é um cascade de botoes é apenas um botão

        
        self.sub_menu_01.add_command(label="Cadastrar", command=self.controle_principal.criar_tela_cadastro_peixe)
        self.sub_menu_01.add_command(label="Mostrar", command=self.controle_principal.mostrar_peixes_cadastrados)


        self.sub_menu_02.add_command(label="Fechamento", command=self.controle_principal.criar_tela_fechar_comanda)

        self.sub_menu_03.add_command(label="Faturamento", command=self.controle_principal.mostrar_faturamento)

        

        # widgets da tela principal

        # self.frame_01 = tk.Frame(self.root)
        # self.frame_01.pack()

        # self.label_01 = tk.Label(self.frame_01, text="Label 01")
        # self.label_01.pack(side="left")

        # self.entry_01 = tk.Entry(self.frame_01)
        # self.entry_01.pack()

        # self.button_01 = tk.Button(self.root, text="Janela Auxiliar", command=self.controle_principal.criar_janela_auxiliar) # adicionei o botão no root e não no frame, fica no final da tela
        # self.button_01.pack(pady=20)
        
        # self.combo_01 = ttk.Combobox(self.root, width=20)
        # self.combo_01['values'] = ['1', '2', '3']
        # self.combo_01.pack()
        
        
        # lista = ['A', 'B', 'C']
        # self.list_box_01 = tk.Listbox(self.root)
        # self.list_box_01.pack()
        # for element in lista:
        #     self.list_box_01.insert(tk.END, element)
        


        self.root.config(menu=self.menu_bar)
        

class ControlePincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tela Principal")
        self.controle_secundario = pagina_secundaria.ControleSecundario(self)


        self.main_view = MainView(self.root, self)
        print("MainView criada")
        self.root.mainloop() # precisa ser o último atributo do ControlePrincipal senão não vai carregar os outros até fechar a MainView


    def criar_janela_auxiliar(self):
        self.auxiliar_view = AuxiliarView(self)
        print("AuxiliarView criada")
        
    def criar_janela_secundaria(self):
        self.controle_secundario.criar_tela_secundaria()
        print("Janela Secundária criada")
        
    def criar_tela_fechar_comanda(self):
        self.controle_secundario.criar_tela_fechar_comanda()
        print("Tela Fechar Comanda criada")
        
    def criar_tela_cadastro_peixe(self):
        self.controle_secundario.criar_tela_cadastro_peixe()
        print("Cadastro Peixe View criada")
        
    def mostrar_peixes_cadastrados(self):
        
        if len(self.controle_secundario.lista_de_peixes) == 0:
            messagebox.showinfo("Lista de Peixes", "Não há peixes cadastrados")
            return
        str = ""
        for peixe in self.controle_secundario.lista_de_peixes:
            str +=  "Nome do peixe: " + peixe.nome + f", Preço  {peixe.preco}"+ "\n"
            
        messagebox.showinfo("Lista de Peixes", str)
        
    def mostrar_faturamento(self):
        self.controle_secundario.mostrar_fatura()
        

    def salva_dados(self):
        # colocar as funções para salvar os dados dos outros controladores aqui
        self.controle_secundario.salvar_instancias()


    def fechar_janela_principal(self):        
        resposta = messagebox.askyesno("Confirmação", "Deseja salvar os dados cadastrados?")
        if resposta == True:
            self.salva_dados()
        
        self.root.destroy()
        



if __name__ == '__main__':
    
    c = ControlePincipal()

