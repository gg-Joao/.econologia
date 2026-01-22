from database import Database

class BaseDAO:
    @staticmethod
    def abrir():
        return Database.conectar()
