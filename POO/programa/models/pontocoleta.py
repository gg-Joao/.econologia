class PontoColeta:
    def __init__(self, id = None, nome = "", endereco ="", fone = "", funcionamento = None, tipoPonto = ""):
        self.set_id(id)
        self.set_nome(nome)
        self.set_endereco(endereco)
        self.set_fone(fone)
        self.set_funcionamento(funcionamento)
        self.set_tipoPonto(tipoPonto)

    def __str__(self):
        return f'ID: {self.get_id()} - NOME {self.get_nome()} - ENDEREÇO {self.get_endereco()} - FONE {self.get_fone()} - HORÁRIO {self.get_funcionamento()} - PONTO {self.get_tipoPonto()}'

    def set_id(self, id):
        self.__id = id
    
    def get_id(self):
        return self.__id
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome
    
    def set_endereco(self, endereco):
        self.__endereco = endereco

    def get_endereco(self):
        return self.__endereco
    
    def set_fone(self, fone):
        self.__fone = fone

    def get_fone(self):
        return self.__fone

    def get_telefone(self):
        return self.__fone
    
    def set_funcionamento(self, funcionamento):
        self.__funcionamento = funcionamento

    def get_funcionamento(self):
        return self.__funcionamento

    def get_horario(self):
        return self.__funcionamento
    
    def set_tipoPonto(self, tipoPonto):
        self.__tipoPonto = tipoPonto

    def get_tipoPonto(self):
        return self.__tipoPonto