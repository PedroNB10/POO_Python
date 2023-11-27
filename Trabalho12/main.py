
import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk



import estudante as est
import equipe as eq
import curso as c




class MainView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root_height = 400
        self.root_width = 400
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        x_cordinate = int((self.screen_width/2) - (self.root_width/2))
        y_cordinate = int((self.screen_height/2) - (self.root_height/2))
        self.root.geometry("{}x{}+{}+{}".format(self.root_width, self.root_height, x_cordinate, y_cordinate))
        
        self.menu_bar = tk.Menu(self.root)

        self.menu_avaliar = tk.Menu(self.menu_bar)
        self.menu_consultar = tk.Menu(self.menu_bar)
        
        self.menu_bar.add_command(label="Criar Equipe", command=self.controller.criar_equipe_view)
        self.menu_bar.add_command(label="Consultar Equipe", command=self.controller.criar_consultar_equipe_view)
        self.menu_bar.add_command(label="Imprimir Dados", command=self.controller.imprimir_dados)
        self.menu_bar.add_command(label="Sair", command=self.controller.fechar_janela)
        self.root.config(menu=self.menu_bar)

        

        self.controleEquipe = eq.ControleEquipe(self.controller)



class ControlePrincipal:
    def __init__(self):
            
        self.root = tk.Tk()
        self.root.title("App de Jogos")
        self.main_view = MainView(self.root, self)
        self.controleEquipe = eq.ControleEquipe(self)
        self.root.mainloop() # precisa ser o ultimo atributo do construtor
        
        
    def fechar_janela(self):
        self.controleEquipe.salvar_equipes()
        self.root.destroy()

    def criar_equipe_view(self):
        self.controleEquipe.criar_equipe_view()

    def criar_consultar_equipe_view(self):
        self.controleEquipe.criar_consultar_equipe_view()


    def imprimir_dados(self):
        str = ''
        if len(self.controleEquipe.listaDeEquipes) == 0:
            messagebox.showinfo('Imprimir Dados', 'Não há equipes cadastradas')
            return
        
        lista_de_equipes = self.controleEquipe.listaDeEquipes
        total_de_equipes = len(lista_de_equipes)
        total_de_estudantes = 0
        for equipe in lista_de_equipes:
            total_de_estudantes += len(equipe.estudantes)
        
        media_de_estudante_por_equipe = total_de_estudantes / total_de_equipes
        str += 'Total de equipes: {}\n'.format(total_de_equipes)
        str += 'Total de estudantes: {}\n'.format(total_de_estudantes)
        str += 'Média de estudantes por equipe: {}\n'.format(media_de_estudante_por_equipe)

        messagebox.showinfo('Imprimir Dados', str)
    
           


if __name__ == "__main__":
    c = ControlePrincipal()
