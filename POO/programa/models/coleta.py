class Coleta:
    def __init__(self, id = None, data = None, confirmado = False, descricao = None, pontos = 0, id_morador = None):
        self.set_id(id)
        self.set_data(data)
        self.set_confirmado(confirmado)
        self.set_desc(descricao)
        self.set_pontos(pontos)
        self.set_id_morador(id_morador)

    def __str__(self):
        return f"ID: {self.get_id()} - ID DO MORADOR: {self.get_id_morador()} DATA: {self.get_data()} - CONFIRMADO: {self.get_confirmado()} - DESCRIÇÃO: {self.get_desc()} - PONTOS: {self.get_pontos()}"

    def set_id(self, id):
        self.__id = id
    
    def get_id(self):
        return self.__id
    
    def set_data(self, data):
        self.__data = data
    
    def get_data(self):
        return self.__data
    
    def set_desc(self, desc):
        self.__desc = desc

    def get_desc(self):
        return self.__desc
    
    def get_descricao(self):
        return self.__desc
    
    def set_confirmado(self, confirmado):
        self.__confirmado = confirmado
    
    def get_confirmado(self):
        return self.__confirmado
    
    def set_pontos(self, pontos):
        self.__pontos = pontos

    def get_pontos(self):
        return self.__pontos

    def set_id_morador(self, id_morador):
        self.__id_morador = id_morador

    def get_id_morador(self):
        return self.__id_morador