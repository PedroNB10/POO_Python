import tkinter as tk
import estudante as est
import curso as c
from tkinter import ttk
import os.path
import pickle



import tkinter.messagebox as messagebox
import tkinter.ttk as ttk

# Rest of your code...
class Equipe: # IMPLEMENTAR
    def __init__(self, curso, estudantes):
        self.__curso = curso
        self.__estudantes = estudantes

    @property
    def curso(self):
        return self.__curso
    
    @property
    def estudantes(self):
        return self.__estudantes

class ConsultarEquipeView(tk.Toplevel):
    def __init__(self, controle):
        self.controle = controle
        tk.Toplevel.__init__(self)
        self.frame_height = 400
        self.frame_width = 400
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        coordenada_x = int((self.screen_width/2) - (self.frame_width/2))
        coordenada_y = int((self.screen_height/2) - (self.frame_height/2))
        self.geometry("{}x{}+{}+{}".format(self.frame_width, self.frame_height, coordenada_x, coordenada_y))
        self.title("Consultar Equipe")
        
        self.frame_principal = tk.Frame(self)
        self.frame_principal.pack(pady=30)
        
        self.label1 = tk.Label(self.frame_principal,text="Digite a sigla do curso: ")
        self.label1.pack(side="left")
        
        self.curso_entry = tk.Entry(self.frame_principal, width=10)
        self.curso_entry.pack()
        
        self.verificar_button = tk.Button(self, text="Verificar", command=self.controle.verificar_equipe_handler)
        self.verificar_button.pack(pady=10)
        
        self.fechar_button = tk.Button(self, text="Fechar", command = lambda: self.controle.fechar_janela(self))
        self.fechar_button.pack(pady=10)
    

class CriarEquipeView(tk.Toplevel):
    def __init__(self, controle):
        self.controle = controle
        tk.Toplevel.__init__(self)
        self.frame_height = 400
        self.frame_width = 400
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        coordenada_x = int((self.screen_width/2) - (self.frame_width/2))
        coordenada_y = int((self.screen_height/2) - (self.frame_height/2))
        self.geometry("{}x{}+{}+{}".format(self.frame_width, self.frame_height, coordenada_x, coordenada_y))
        self.title("Criar Equipe")

        self.frame_principal = tk.Frame(self)
        self.frame_principal.pack(pady=30)

        self.frame_secundario = tk.Frame(self)
        self.frame_secundario.pack(pady=5)
        
        self.label1 = tk.Label(self.frame_principal,text="Nome dos cursos: ")
        self.label1.pack(side="left")

        self.combobox1 = ttk.Combobox(self.frame_principal, width=20)
        self.combobox1.pack(side="left")
        self.combobox1['values'] = [curso.getNome for curso in self.controle.listaCurso]


        self.label2 = tk.Label(self.frame_secundario,text="Nro de Matricula do estudante selecionado:")
        self.label2.pack(side="left")

        self.estudante_entry = tk.Entry(self.frame_secundario, width=10)
        self.estudante_entry.pack(side="left")


        self.adicionar_button = tk.Button(self, text="Adicionar Aluno", command=self.controle.adicionar_aluno_equipe_handler)
        self.adicionar_button.pack(pady=10)

        self.submit_button = tk.Button(self, text="Criar Equipe", command=self.controle.criar_equipe)
        self.submit_button.pack(pady=10)
        
        self.fechar_button = tk.Button(self, text="Fechar", command = lambda: self.controle.fechar_janela(self))
        self.fechar_button.pack(pady=10)

class ImprimirDadosView(tk.Toplevel):
    def __init__(self, controle):
        self.controle = controle
        tk.Toplevel.__init__(self)
        self.frame_height = 400
        self.frame_width = 400
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        coordenada_x = int((self.screen_width/2) - (self.frame_width/2))
        coordenada_y = int((self.screen_height/2) - (self.frame_height/2))
        self.geometry("{}x{}+{}+{}".format(self.frame_width, self.frame_height, coordenada_x, coordenada_y))
        self.title("Imprimir Dados")
        
        


class ControleEquipe:
    def __init__(self, controlePrincipal):
        self.controlePrincipal = controlePrincipal
        if not os.path.isfile("equipes.pickle"):
            self.listaDeEquipes = []
            self.dicionario_equipes = {}
        else:
            with open("equipes.pickle", "rb") as f:
                self.listaDeEquipes = pickle.load(f)
                self.dicionario_equipes = {Equipe.curso.getSigla: Equipe for Equipe in self.listaDeEquipes } # dicionario de equipes
                
                for equipe in self.listaDeEquipes:
                    print(equipe.curso.getNome)
                    for estudante in equipe.estudantes:
                        print(estudante.getNome)
        c1 = c.Curso("CCO", "Ciência da Computação")
        c2 = c.Curso("SIN", "Sistemas de Informação")
        c3 = c.Curso("EEL", "Engenharia Elétrica")
        self.listaCurso = []
        self.listaCurso.append(c1)
        self.listaCurso.append(c2)
        self.listaCurso.append(c3)
        #Inserir mais cursos, se quiser
        self.listaEstudante = []
        self.listaEstudante.append(est.Estudante(1001, "José da Silva", c1))
        self.listaEstudante.append(est.Estudante(1002, "João de Souza", c1))
        self.listaEstudante.append(est.Estudante(1003, "Rui Santos", c2))
        self.listaEstudante.append(est.Estudante(1004, "Maria Oliveira", c2))
        self.listaEstudante.append(est.Estudante(1005, "Pedro Nogueira", c2))
        self.listaEstudante.append(est.Estudante(1006, "Ana Costa", c3))
        self.listaEstudante.append(est.Estudante(1007, "Luiz Pereira", c1))
        self.listaEstudante.append(est.Estudante(1008, "Mariana Santos", c3))
        self.listaEstudante.append(est.Estudante(1009, "Carlos Silva", c1))
        self.listaEstudante.append(est.Estudante(1010, "Juliana Oliveira", c2))
        self.listaEstudante.append(est.Estudante(1011, "Rafaela Costa", c3))
        self.lista_temp = []

    
        
        
        

    def salvar_equipes(self):
        if len(self.listaDeEquipes) != 0:
            with open('equipes.pickle', 'wb') as f:
                pickle.dump(self.listaDeEquipes, f)

    
    def verificar_equipe_handler(self):
        sigla = self.consultarEquipeView.curso_entry.get()
        for curso in self.listaCurso:
            if curso.getSigla == sigla and curso.getSigla not in self.dicionario_equipes:
                
                messagebox.showinfo("Curso encontrado", "Curso existe porém não há equipes desse curso!")
                return
            elif curso.getSigla == sigla and curso.getSigla in self.dicionario_equipes:
                str = ''
                c = 1
                str += f"Curso:{curso.getNome}\n \n"
                for equipe in self.listaDeEquipes:
                    if equipe.curso.getSigla == sigla:
                        
                        str += "Equipe "
                        str += f"{c}\n"
                        for estudante in equipe.estudantes:
                            str += '- '+ estudante.getNome + "\n"
                            
                        c += 1
                        str += "\n"
                messagebox.showinfo("Curso encontrado", str)
                return
              
        messagebox.showerror("Erro", "Equipe inexistente")

    def verificar_se_aluno_tem_equipe(self, matricula):
        for equipe in self.listaDeEquipes:
            for estudante in equipe.estudantes:
                if estudante.getNroMatric == matricula:
                    return True
        return False
    
    def verificar_se_aluno_esta_na_equipe(self, matricula):
        for aluno in self.lista_temp:
            if aluno.getNroMatric == matricula:
                return True
        return False
        
    def criar_equipe(self):
        if len(self.lista_temp) == 0:
            curso = self.criarEquipeView.combobox1.get()
        else:
            curso = self.lista_temp[0].getCurso
        equipe = Equipe(curso, self.lista_temp)
        self.listaDeEquipes.append(equipe)
        
        if self.dicionario_equipes.get(curso.getSigla) == None:
            self.dicionario_equipes[curso.getSigla] = []
            self.dicionario_equipes[curso.getSigla].append(equipe)
            
        else:
            self.dicionario_equipes[curso.getSigla].append(equipe)
 


        print("Equipe criada com sucesso")
        print("Curso: ", equipe.curso.getNome)
        print("Estudantes: ")
        for estudante in equipe.estudantes:
            print(estudante.getNome)
        
        self.lista_temp = []
        messagebox.showinfo("Sucesso", "Equipe criada com sucesso")
        self.criarEquipeView.destroy()

    
    def adicionar_aluno_equipe_handler(self):
        
        matricula = self.criarEquipeView.estudante_entry.get()
        curso = self.criarEquipeView.combobox1.get()

        try:
            print(matricula)
            matricula = int(matricula)
        except:
            messagebox.showerror("Erro", "Matricula deve ser um número inteiro")
            return

        for estudante in self.listaEstudante:
            if estudante.getNroMatric == matricula and estudante.getCurso.getNome == curso:
                
                if self.verificar_se_aluno_esta_na_equipe(matricula):
                    messagebox.showerror("Erro", "Aluno já está na equipe")
                    return
                
                if self.verificar_se_aluno_tem_equipe(matricula):
                    messagebox.showerror("Erro", "Aluno já está em uma equipe")
                    return
                
                if len(self.lista_temp) > 0:
                    if self.lista_temp[0].getCurso.getNome == curso:
                        self.lista_temp.append(estudante)
                        messagebox.showinfo("Sucesso", "Aluno adicionado na equipe")
                        return
                    else:
                        messagebox.showerror("Erro", "Aluno não está no mesmo curso da equipe")
                        return
                self.lista_temp.append(estudante)
                messagebox.showinfo("Sucesso", "Aluno adicionado na equipe")
                return
        messagebox.showerror("Erro", "Aluno não encontrado")
        
    def fechar_janela(self, janela):
        janela.destroy()

    def criar_equipe_view(self):
        self.criarEquipeView = CriarEquipeView(self)
        
    def criar_consultar_equipe_view(self):
        self.consultarEquipeView = ConsultarEquipeView(self)

    def criar_consultar_equipe_view(self):
        self.consultarEquipeView = ConsultarEquipeView(self)
    # def consultar_equipe_view(self):
    #     self.consultarEquipeView = ConsultarEquipeView(self)

    # def imprimir_dados_view(self):
    #     self.imprimirDadosView = ImprimirDadosView(self)
