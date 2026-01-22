class SolicitacaoRecompensa:
    def __init__(self, id = None, morador_id = None, recompensa_id = None, data = None, status = "pendente"):
        self.set_id(id)
        self.set_morador_id(morador_id)
        self.set_recompensa_id(recompensa_id)
        self.set_data(data)
        self.set_status(status)

    def __str__(self):
        return f'ID: {self.get_id()} - MORADOR: {self.get_morador_id()} - RECOMPENSA: {self.get_recompensa_id()} - DATA: {self.get_data()} - STATUS: {self.get_status()}'

    def set_id(self, id):
        self.__id = id
    
    def get_id(self):
        return self.__id

    def set_morador_id(self, morador_id):
        self.__morador_id = morador_id
    
    def get_morador_id(self):
        return self.__morador_id

    def set_recompensa_id(self, recompensa_id):
        self.__recompensa_id = recompensa_id
    
    def get_recompensa_id(self):
        return self.__recompensa_id

    def set_data(self, data):
        self.__data = data
    
    def get_data(self):
        return self.__data
    
    def set_status(self, status):
        self.__status = status
    
    def get_status(self):
        return self.__status