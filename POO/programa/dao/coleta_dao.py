from dao.base_dao import BaseDAO
from models.coleta import Coleta
from datetime import datetime

class ColetaDAO(BaseDAO):

    @staticmethod
    def inserir(obj):
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO coleta (data, confirmado, descricao, pontos) VALUES (?, ?, ?, ?)",
            (obj.get_data() if isinstance(obj.get_data(), str) else obj.get_data().isoformat(), 
             int(obj.get_confirmado()), obj.get_desc(), obj.get_pontos()) )
        conn.commit()
        conn.close()

    @staticmethod
    def listar():
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM coleta")
        dados = cursor.fetchall()
        conn.close()

        lista = []
        for d in dados:
            coleta = Coleta(d[0], d[1], bool(d[2]), d[3], d[4])
            lista.append(coleta)
        return lista

    @staticmethod
    def buscar_por_id(id):
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM coleta WHERE id = ?", (id,))
        dado = cursor.fetchone()
        conn.close()

        if dado:
            return Coleta(dado[0], dado[1], bool(dado[2]), dado[3], dado[4])
        return None

    @staticmethod
    def atualizar(obj):
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE coleta SET data = ?, confirmado = ?, descricao = ?, pontos = ?
            WHERE id = ?
        """, (obj.get_data(), int(obj.get_confirmado()), obj.get_desc(), obj.get_pontos(), obj.get_id()))
        conn.commit()
        conn.close()

    @staticmethod
    def deletar(id):
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM coleta WHERE id = ?", (id,))
        conn.commit()
        conn.close()
