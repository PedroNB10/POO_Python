

class username_duplicado(Exception):
    pass

class email_invalido(Exception):
    pass

class idade_menor_que_permitida(Exception):
    pass

class idade_invalida(Exception):
    pass

class User:
    def __init__(self,username, email):
        self.__username = username
        self.__email = email
        
    @property
    def username(self):
        return self.__username
    
    @property
    def email(self):
        return self.__email
    
    @username.setter
    def username(self,username):
        self.__username = username
        
    @email.setter
    def email(self,email):
        self.__email = email
        
        
if __name__ == "__main__":
    listaExemplo = [
        ("Paulo", "paulo@gmail.com", 21), 
        ("Paulo", "paulo@gmail.com", 21), 
        ("Ednaldo Pereira", "Ednaldopereira.chansey@yahoo.com.br",10000),
        ("antonio", "antonio@gmail.com", 15),
        ("maria", "maria@", 18),
        ("cirilo", "cirilo@gmail.com",-23)
    ]
    
    cadastro = {}
    
    for username, email, idade in listaExemplo:
    
        try:
            if username in cadastro:
                raise username_duplicado
            if idade < 0:
                raise idade_invalida
            if idade < 18:
                raise idade_menor_que_permitida
            
            email_dividido = email.split("@") # ["nome", "dominio"] remove o @ e divide a string 
            
            if len(email_dividido) != 2 or not email_dividido[0] or not email_dividido[1]: # nao pode ser uma unica string ou ser uma string vazia
                raise email_invalido
            

        except username_duplicado:
            print("O username", username, "já está cadastrado!")

                
        except idade_invalida:
            print("A idade", idade, "é inválida!")
            
        except idade_menor_que_permitida:
            print("A idade", idade, "é menor que a permitida!")
            
        except email_invalido:
            print("O email", email, "é inválido!")
            
        else:
            cadastro[username] = User(username, email)
            
    print("Usuarios cadastrados")   
    for username in cadastro:
        
        print(cadastro[username].username, cadastro[username].email)