class Usuario:
    def __init__(self, email, fone, senha):
        self.set_email(email)
        self.set_fone(fone)
        self.set_senha(senha)
    
    def __str__(self):
        return f"{self.nome} ({self.pontos} pontos)"

    def set_id(self, id):
        self.__id = id

    def set_email(self, email):
        self.__email = email

    def set_fone(self, fone):
        self.__fone = fone

    def set_senha(self, senha):
        self.__senha = senha
        
    def get_id(self):
        return self.__id
        
    def get_email(self):
        return self.__email
        
    def get_fone(self):
        return self.__fone
        
    def get_senha(self):
        return self.__senha