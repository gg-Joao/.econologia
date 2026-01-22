from models.usuario import Usuario

class cooperativa(Usuario):
    def __init__(self, id = None, razaoSocial = "", cnpj = 0, email = "", endereco = "", fone = 0, senha = ""):
        self.set_id(id)
        self.set_razao(razaoSocial)
        self.set_cnpj(cnpj)
        self.set_email(email)
        self.set_endereco(endereco)
        self.set_fone(fone)
        self.set_senha(senha)

    def __str__(self):
        return f'ID: {self.get_id()} - RAZÃO: {self.get_razao()} - CNPJ: {self.get_cnpj()} - EMAIL: {self.get_email()} - ENDEREÇO: {self.get_endereco()} - FONE: {self.get_fone()} - SENHA: {self.get_senha()}'

    def set_razao(self, razao):
        self.__razao = razao
    
    def get_razao(self):
        return self.__razao
    
    def set_cnpj(self, cnpj):
        self.__cnpj = cnpj

    def get_cnpj(self):
        return self.__cnpj
    
    def set_endereco(self, endereco):
        self.__endereco = endereco

    def get_endereco(self):
        return self.__endereco
    