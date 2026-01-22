from datetime import datetime

class Recompensa:
    def __init__(self, id, nome, descricao, pontosNecessarios, tipoRecompensa, validade):
        self.set_id(id)
        self.set_nome(nome)
        self.set_descricao(descricao)
        self.set_pontos(pontosNecessarios)
        self.set_tipoRecompensa(tipoRecompensa)
        self.set_validade(validade)

    def __str__(self):
        return f'NOME: {self.get_nome()} - DESCRIÇÃO {self.get_descricao()} - PONTOS {self.get_pontos()}'

    def set_id(self, id):
        self.__id = id
    
    def get_id(self):
        return self.__id

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome
    
    def set_descricao(self, desc):
        self.__desc = desc

    def get_descricao(self):
        return self.__desc
    
    def set_pontos(self, pontos):
        self.__pontos = pontos

    def get_pontos(self):
        return self.__pontos
    
    def set_tipoRecompensa(self, tipoRecompensa):
        self.__tipoRecompensa = tipoRecompensa

    def get_tipoRecompensa(self):
        return self.__tipoRecompensa
    
    def set_validade(self, validade):
        self.__validade = validade

    def get_validade(self):
        return self.__validade