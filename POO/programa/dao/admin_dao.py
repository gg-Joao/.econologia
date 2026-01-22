from dao.base_dao import BaseDAO
from models.admin import Admin

class AdminDAO:

    @staticmethod
    def inserir(admin):
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO admin (nome, email, senha)
            VALUES (?, ?, ?)
        """, (admin.get_nome(), admin.get_email(), admin.get_senha()))
        conn.commit()
        conn.close()

    @staticmethod
    def login(email, senha):
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM admin WHERE email=? AND senha=?
        """, (email, senha))
        dado = cursor.fetchone()
        conn.close()

        if dado:
            return Admin(dado[0], dado[1], dado[2], dado[3])
        return None

    @staticmethod
    def listar():
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM admin")
        dados = cursor.fetchall()
        conn.close()

        return [Admin(d[0], d[1], d[2], d[3]) for d in dados]
