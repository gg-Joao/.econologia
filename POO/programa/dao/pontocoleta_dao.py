from dao.base_dao import BaseDAO
from models.pontocoleta import PontoColeta

class PontoColetaDAO:

    @staticmethod
    def inserir(obj):
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO pontocoleta (nome, endereco, telefone, horario)
            VALUES (?, ?, ?, ?)
        """, (obj.get_nome(), obj.get_endereco(), obj.get_telefone(), obj.get_horario()))
        conn.commit()
        conn.close()

    @staticmethod
    def listar():
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pontocoleta")
        dados = cursor.fetchall()
        conn.close()

        if dados:
            return [PontoColeta(d[0], d[1], d[2], d[3], d[4]) for d in dados]
        return []

    @staticmethod
    def buscar_por_id(id):
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pontocoleta WHERE id = ?", (id,))
        dado = cursor.fetchone()
        conn.close()

        if dado:
            return PontoColeta(dado[0], dado[1], dado[2], dado[3], dado[4])
        return None

    @staticmethod
    def atualizar(obj):
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE pontocoleta SET nome = ?, endereco = ?, telefone = ?, horario = ?
            WHERE id = ?
        """, (obj.get_nome(), obj.get_endereco(), obj.get_telefone(), obj.get_horario(), obj.get_id()))
        conn.commit()
        conn.close()

    @staticmethod
    def deletar(id):
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM pontocoleta WHERE id = ?", (id,))
        conn.commit()
        conn.close()
