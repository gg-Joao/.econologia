from models.usuario import Usuario

class Morador(Usuario):
    def __init__(self, id=None, nome="", email="", fone=0, pontos=0, senha=""):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_pontos(pontos)
        self.set_senha(senha)

    def __str__(self):
        return f"ID: {self.get_id()} - NOME: {self.get_nome()} - EMAIL: {self.get_email()} - FONE: {self.get_fone()} - PONTOS: ({self.get_pontos()}) - SENHA: {self.get_senha()}"
    
    def set_nome(self, nome):
        self.__nome = nome

    def set_pontos(self, pontos):
        self.__pontos = pontos

    def get_nome(self):
        return self.__nome
    
    def get_pontos(self):
        return self.__pontos