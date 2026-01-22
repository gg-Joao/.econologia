from dao.base_dao import BaseDAO
from models.recompensa import Recompensa

class RecompensaDAO:

    @staticmethod
    def inserir(obj):
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO recompensa (nome, descricao, pontosnecessarios, tiporecompensa, validade)
            VALUES (?, ?, ?, ?, ?)
        """, (obj.get_nome(), obj.get_descricao(), obj.get_pontos(), obj.get_tipoRecompensa(), obj.get_validade()))
        conn.commit()
        conn.close()

    @staticmethod
    def listar():
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM recompensa")
        dados = cursor.fetchall()
        conn.close()

        if dados:
            return [Recompensa(d[0], d[1], d[2], d[3], d[4], d[5]) for d in dados]
        return []

    @staticmethod
    def buscar_por_id(id):
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM recompensa WHERE id = ?", (id,))
        dado = cursor.fetchone()
        conn.close()

        if dado:
            return Recompensa(dado[0], dado[1], dado[2], dado[3], dado[4], dado[5])
        return None

    @staticmethod
    def atualizar(obj):
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE recompensa SET nome = ?, descricao = ?, pontosnecessarios = ?, tiporecompensa = ?, validade = ?
            WHERE id = ?
        """, (obj.get_nome(), obj.get_descricao(), obj.get_pontos(), obj.get_tipoRecompensa(), obj.get_validade(), obj.get_id()))
        conn.commit()
        conn.close()

    @staticmethod
    def deletar(id):
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM recompensa WHERE id = ?", (id,))
        conn.commit()
        conn.close()
