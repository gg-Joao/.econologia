from dao.base_dao import BaseDAO
from models.solicitacao_recompensa import SolicitacaoRecompensa

class SolicitacaoRecompensaDAO:

    @staticmethod
    def inserir(obj):
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO solicitacao_recompensa (morador_id, recompensa_id, data, status)
            VALUES (?, ?, ?, ?)
        """, (obj.get_morador_id(), obj.get_recompensa_id(), obj.get_data(), obj.get_status()))
        conn.commit()
        conn.close()

    @staticmethod
    def listar():
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM solicitacao_recompensa")
        dados = cursor.fetchall()
        conn.close()
        if dados:
            return [SolicitacaoRecompensa(d[0], d[1], d[2], d[3], d[4]) for d in dados]
        return []

    @staticmethod
    def listar_por_morador(morador_id):
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM solicitacao_recompensa WHERE morador_id = ?", (morador_id,))
        dados = cursor.fetchall()
        conn.close()

        if dados:
            return [SolicitacaoRecompensa(d[0], d[1], d[2], d[3], d[4]) for d in dados]
        return []

    @staticmethod
    def buscar_por_id(id):
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM solicitacao_recompensa WHERE id = ?", (id,))
        dado = cursor.fetchone()
        conn.close()

        if dado:
            return SolicitacaoRecompensa(dado[0], dado[1], dado[2], dado[3], dado[4])
        return None

    @staticmethod
    def atualizar(obj):
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE solicitacao_recompensa SET morador_id = ?, recompensa_id = ?, data = ?, status = ?
            WHERE id = ?
        """, (obj.get_morador_id(), obj.get_recompensa_id(), obj.get_data(), obj.get_status(), obj.get_id()))
        conn.commit()
        conn.close()

    @staticmethod
    def deletar(id):
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM solicitacao_recompensa WHERE id = ?", (id,))
        conn.commit()
        conn.close()
