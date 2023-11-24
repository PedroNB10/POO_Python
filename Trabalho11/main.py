import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os.path
import pickle

# exepctions


class Jogo:
    def __init__(self, codigo, titulo, console, genero, preco):
        self.consoles = ['Xbox', 'Playstation', 'PC', 'Switch']
        self.generos = ['Ação', 'Aventura', 'Esporte', 'Estratégia', 'RPG', 'Simulação']
        
        self.codigo = codigo
        self.__titulo = titulo
        self.console = console # chama o setter
        self.genero = genero
        self.preco = preco
        self.__avaliacoes = []
        
        

    
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        try:
            codigo = int(codigo)
            self.__codigo = codigo
        except:
            raise ValueError("Código deve ser um número inteiro")
            
    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def console(self):
        return self.__console
    
    @console.setter
    def console(self, console):

        if console.capitalize() not in self.consoles:
            raise ValueError(f"Console inválido: {console}")
        else:
            self.__console = console.capitalize()
            
    
    @property
    def genero(self):
        return self.__genero
    
    @genero.setter
    def genero(self, genero):
        
        if genero.capitalize() not in self.generos:
            raise ValueError(f"Gênero inválido: {genero}")
        else:

            self.__genero = genero.capitalize()
    
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, preco):
        try:
            preco = float(preco)
            self.__preco = preco
        except:
            raise ValueError("Preço deve ser um número")
    
    @property
    def avaliacoes(self):
        return self.__avaliacoes
    
class ConsultarView(tk.Toplevel):
    def __init__(self, root, controller):
        super().__init__()
        self.title("Consultar Jogo")
        self.root = root
        self.controller = controller
        self.window_height = 400
        self.window_width = 300
        self.screen_width = controller.root.winfo_screenwidth()
        self.screen_height = controller.root.winfo_screenheight()
        x_cordinate = int((self.screen_width/2) - (self.window_width/2))
        y_cordinate = int((self.screen_height/2) - (self.window_height/2))
        self.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, x_cordinate, y_cordinate))


        self.frame_principal = tk.Frame(self)
        self.frame_principal.pack()
        self.titulo = tk.Label(self.frame_principal, text="Consultar Jogo", font=("Arial", 11), pady=10)
        self.titulo.pack()
        self.frame_combo_box = tk.Frame(self.frame_principal)
        self.frame_combo_box.pack(pady=(20,0))

        self.label_nota = tk.Label(self.frame_combo_box, text="Nota: ")
        self.label_nota.pack(side="left")

        self.combo_nota = ttk.Combobox(self.frame_combo_box, values=[1,2,3,4,5])
        self.combo_nota.pack()
        self.combo_nota.bind("<<ComboboxSelected>>", self.controller.atualizar_listbox_handler)

        self.listbox = tk.Listbox(self.frame_principal, width=30, height=10)
        self.listbox.pack(pady=(20,0))

        for jogo in self.controller.lista_de_jogos:
            self.listbox.insert(tk.END, jogo.titulo)

        self.destroy_button = tk.Button(self.frame_principal, text="Fechar")
        self.destroy_button.pack(pady=(5,0))
        self.destroy_button.bind("<Button>", self.controller.destruir_consultar_view_handler)

      



class AvaliacaoView(tk.Toplevel):
    def __init__(self, root, controller):
        super().__init__()
        self.title("Avaliar Jogo")
        self.root = root
        self.controller = controller
        self.window_height = 300
        self.window_width = 300
        self.screen_width = controller.root.winfo_screenwidth()
        self.screen_height = controller.root.winfo_screenheight()
        x_cordinate = int((self.screen_width/2) - (self.window_width/2))
        y_cordinate = int((self.screen_height/2) - (self.window_height/2))
        self.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, x_cordinate, y_cordinate))


        self.frame_principal = tk.Frame(self)
        self.frame_principal.pack()
        self.titulo = tk.Label(self.frame_principal, text="Avaliação do Jogo", font=("Arial", 11), pady=10)
        self.titulo.pack()
        self.frame_codigo = tk.Frame(self.frame_principal)
        self.frame_codigo.pack(pady=(20,0))
        self.frame_nota = tk.Frame(self.frame_principal)
        self.frame_nota.pack(pady=(20,0))
 
    

        self.label_codigo = tk.Label(self.frame_codigo, text="Código do Jogo: ")
        self.label_codigo.pack(side="left")
        self.entry_codigo = tk.Entry(self.frame_codigo)
        self.entry_codigo.pack()

        self.label_nota = tk.Label(self.frame_nota, text="Nota: ")
        self.label_nota.pack(side="left")
        self.combo_nota = ttk.Combobox(self.frame_nota, values=[1,2,3,4,5])
        self.combo_nota.pack()



        self.submit_button = tk.Button(self.frame_principal, text="Avaliar")
        self.submit_button.pack(pady=(20,0))
        self.submit_button.bind("<Button>", self.controller.avaliar_jogo_handler)
        
        self.destroy_button = tk.Button(self.frame_principal, text="Fechar")
        self.destroy_button.pack(pady=(20,0))
        self.destroy_button.bind("<Button>", self.controller.destruir_avaliacao_view_handler)






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
        
        self.menu_bar.add_command(label="Avaliar", command= self.controller.criar_avaliacao_view)
        self.menu_bar.add_command(label="Listar", command= self.controller.criar_consultar_view)
        self.menu_bar.add_command(label="Jogos Cadastrados", command= self.controller.mostrar_jogos_cadastrados)
        self.menu_bar.add_command(label="Sair", command= self.controller.sair_do_app)
        

        self.frame_principal = tk.Frame(self.root)
        self.frame_principal.pack()

        self.frame_codigo = tk.Frame(self.root)
        self.frame_codigo.pack(pady=(20,0))

        self.frame_titulo = tk.Frame(self.root)
        self.frame_titulo.pack(pady=(15,15))

        self.frame_console = tk.Frame(self.root)
        self.frame_console.pack(pady=(0,15))

        self.frame_genero = tk.Frame(self.root)
        self.frame_genero.pack(pady=(0,15))

        self.frame_preco = tk.Frame(self.root)
        self.frame_preco.pack()

        self.titulo = tk.Label(self.frame_principal, text="Cadastro de Jogo", font=("Arial", 13), pady=10)
        self.titulo.pack()

        self.label_codigo = tk.Label(self.frame_codigo, text="Código: ")
        self.label_codigo.pack(side="left")
        self.entry_codigo = tk.Entry(self.frame_codigo)
        self.entry_codigo.pack()

        self.label_titulo = tk.Label(self.frame_titulo, text="Título: ")
        self.label_titulo.pack(side="left")
        self.entry_titulo = tk.Entry(self.frame_titulo)
        self.entry_titulo.pack()

        self.label_console = tk.Label(self.frame_console, text="Console: ")
        self.label_console.pack(side="left")
        self.entry_console = tk.Entry(self.frame_console)
        self.entry_console.pack()

        self.label_genero = tk.Label(self.frame_genero, text="Genero: ")
        self.label_genero.pack(side="left")
        self.entry_genero = tk.Entry(self.frame_genero)
        self.entry_genero.pack()

        self.label_preco = tk.Label(self.frame_preco, text="Preço: ")
        self.label_preco.pack(side="left")
        self.entry_preco = tk.Entry(self.frame_preco)
        self.entry_preco.pack()

        self.submit_button = tk.Button(self.root, text="Cadastrar")
        self.submit_button.bind("<Button>", controller.cadastrar_handler)
        self.submit_button.pack(pady=(20,0))


        self.root.config(menu=self.menu_bar)
        
    def mostrar_mensagem(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

class mainController:
    def __init__(self):
        
        if not os.path.isfile("jogos.pickle"):
           self.lista_de_jogos = []
        else:
            # para funcionar tem que estar no mesmo diretório do vscode
            with open("jogos.pickle", "rb") as f:
                self.lista_de_jogos = pickle.load(f)
        

        self.root = tk.Tk()
        self.root.title("App de Jogos")
        self.main_view = MainView(self.root, self)
        self.root.mainloop()

    def salvar_dados(self):
        if len(self.lista_de_jogos) != 0:
            with open("jogos.pickle", "wb") as f:
                pickle.dump(self.lista_de_jogos, f)

    def destruir_avaliacao_view_handler(self, event):
        self.avaliacao_view.destroy()

    def destruir_consultar_view_handler(self, event):
        self.consultar_view.destroy()

    def atualizar_listbox_handler(self, event):
        self.consultar_view.listbox.delete(0, tk.END)
        nota_selecionada = self.consultar_view.combo_nota.get()
        jogos_filtrados = self.filtrar_jogos_por_nota(int(nota_selecionada))

        
        for jogo in jogos_filtrados:
            self.consultar_view.listbox.insert(tk.END, jogo)


        

    def filtrar_jogos_por_nota(self, nota):

        jogos_filtrados = []
        for jogo in self.lista_de_jogos:

                if len(jogo.avaliacoes) > 0:
                    media = sum(jogo.avaliacoes) / len(jogo.avaliacoes)
                    print(f'média do jogo {jogo.titulo}: {media}')
                else:
                    continue

                if media >= 0 and media <= 1:
                    media = 1
                elif media > 1 and media <= 2:
                    media = 2
                elif media > 2 and media <= 3:
                    media = 3
                elif media > 3 and media <= 4:
                    media = 4
                elif media > 4 and media <= 5:
                    media = 5

                if media == nota:
                    jogos_filtrados.append(jogo.titulo)
        return jogos_filtrados
    

    def mostrar_jogos_cadastrados(self):
        str = ''
        for jogo in self.lista_de_jogos:
            str += f'Código: {jogo.codigo}\nTítulo: {jogo.titulo}\nConsole: {jogo.console}\nGênero: {jogo.genero}\nPreço: {jogo.preco} \n'
            if len(jogo.avaliacoes)  == 0:
                str += 'Nenhuma avaliação realizada\n'
                str += '------\n'
                continue
            str += f'Avaliações:\n'
            for  idx, avaliacao in enumerate(jogo.avaliacoes):

                str += f'user[{idx + 1}]: {avaliacao}\n'
            str += '------\n'
        messagebox.showinfo("Jogos Cadastrados", str)

    def sair_do_app(self):
        resposta = messagebox.askyesno("Sair", "Deseja salvar os dados cadastrados ?")
        print(resposta)

        if resposta: # se resposta for sim
            self.salvar_dados()
        
        self.root.destroy()

    def jogo_existe(self, codigo):
        for jogo in self.lista_de_jogos:
            if jogo.codigo == codigo:
                return True
        return False
    
    def mostrar_mensagem(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

    def criar_avaliacao_view(self):
        self.avaliacao_view = AvaliacaoView(self.root, self)

    def criar_consultar_view(self):
        self.consultar_view = ConsultarView(self.root, self)


    def avaliar_jogo_handler(self, event):
        codigo = self.avaliacao_view.entry_codigo.get()
        nota = self.avaliacao_view.combo_nota.get()

        try:
            codigo = int(codigo)
        
        except:
            print("Código inválido")
            
            messagebox.showerror("Erro", f"Código {codigo} é  inválido")
            self.avaliacao_view.lift() # traz a janela para frente
            return 

        if self.jogo_existe(codigo):
            for jogo in self.lista_de_jogos:
                if jogo.codigo == codigo:
                    jogo.avaliacoes.append(int(nota))
                    print("Avaliação realizada com sucesso!")
                    
                    messagebox.showinfo("Sucesso", "Jogo avaliado com sucesso!")
                    self.avaliacao_view.lift()
                    return
        else:
            print("Jogo não encontrado")
           
            messagebox.showerror("Erro", "Jogo não encontrado")
            self.avaliacao_view.lift()
            return

    def cadastrar_handler(self, event):

        codigo = self.main_view.entry_codigo.get()
        titulo = self.main_view.entry_titulo.get()
        console = self.main_view.entry_console.get()
        preco = self.main_view.entry_preco.get()
        genero = self.main_view.entry_genero.get()

        if codigo == "" or titulo == "" or console == "" or preco == "" or genero == "":
            messagebox.showerror("Erro", "Preencha todos os campos")
            return


        titulo = titulo.title()
        console = console.capitalize()
        genero = genero.capitalize()

        try:
        
            jogo = Jogo(codigo, titulo, console, genero, preco)
            if self.jogo_existe(jogo.codigo):
                messagebox.showerror("Erro", "Jogo já cadastrado")
                return
            else:
                self.lista_de_jogos.append(jogo)
                messagebox.showinfo("Sucesso", "Jogo cadastrado com sucesso!")

        except ValueError as error:
            self.main_view.mostrar_mensagem("Erro", error)
            return
        
        self.main_view.entry_codigo.delete(0, tk.END)
        self.main_view.entry_titulo.delete(0, tk.END)
        self.main_view.entry_console.delete(0, tk.END)
        self.main_view.entry_preco.delete(0, tk.END)
        self.main_view.entry_genero.delete(0, tk.END)


if __name__ == "__main__":
    m = mainController()