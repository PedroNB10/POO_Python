

# para livros
class nomeLivroInvalido(Exception):
    pass

class autorInvalido(Exception):
    pass

class anoInvalido(Exception):
    pass

# para usuários
class nomeInvalido(Exception):
    pass

class numeroTelefoneInvalido(Exception):
    pass

class enderecoInvalido(Exception):
    pass

class usuarioDuplicado(Exception):
    pass


class Livro:
    def __init__(self, titulo, autor, ano_publicacao, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicado = ano_publicacao
        self.num_paginas = num_paginas
        



class Usuario:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        


if __name__ == "__main__":
    
    lista_de_usuarios = [
                         ("Pedro","35999545259","pedro.nogueira.barboza@gmail.com"),
                         ("Ana","19387439256","ana.b@outlook.om"),
                         ("B","45629548249","bias@yahoo.com"),
                         ("Joao","39829304781","ednaldo@eliot.com"),
                         ("Maria","35999545259","sldkms@mmm.com "),
                        ]
    
    lista_de_livros = [
                          ("O Senhor dos Anéis","J. R. R. Tolkien",1954, 1000),
                          ("O Pequeno Príncipe","Antoine de Saint-Exupéry",1943, 100),
                          ("A Menina que Roubava Livros","Markus Zusak",2005, 200),
                          ("Cem Anos de Solidão","Gabriel García Márquez",1967, 300),
                          ("Dom Quixote","Miguel de Cervantes",1605, 400),
                          ("Sol da Meia-Noite","Stephenie Meyer",2020, 500),
                        ]
    
    
    # cadastro usuarios
    
    usuarios_cadastrados = {}
    
    for nome, telefone, email in lista_de_usuarios:
        
        try:
            if telefone in usuarios_cadastrados:
                raise usuarioDuplicado
            elif len(telefone) != 11:
                raise numeroTelefoneInvalido
            elif "@" not in email or ".com" not in email:
                raise enderecoInvalido
            elif len(nome) < 2 or len(nome) > 50:
                raise nomeInvalido
            else:
                usuarios_cadastrados[telefone] = Usuario(nome, telefone, email)
                
        except usuarioDuplicado:
            print("Usuário "+nome+" possui o número de telefone "+telefone+" que já foi cadastrado!")
        except numeroTelefoneInvalido:
            print(f"Número de telefone do {nome} inválido!")
        except enderecoInvalido:
            print(f"o endereço de email {email} não é um endereço válido!")
        except nomeInvalido:
            print(f"O nome {nome}  não é um nome válido!")
            
    print("Usuários cadastrados:")
    
    for telefone in usuarios_cadastrados:
        print(usuarios_cadastrados[telefone].nome)
        print(telefone)
        print(usuarios_cadastrados[telefone].email)

            
            
            