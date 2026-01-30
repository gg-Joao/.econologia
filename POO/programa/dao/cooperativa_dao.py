from dao.base_dao import BaseDAO
from models.cooperativa import cooperativa

class CooperativaDAO:

    @staticmethod
    def inserir(coop):
        if CooperativaDAO.verificar_email(coop.get_email()):
            raise ValueError("Email já cadastrado")
        if CooperativaDAO.verificar_cnpj(coop.get_cnpj()):
            raise ValueError("CNPJ já cadastrado")
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO cooperativa (razao_social, cnpj, email, endereco, fone, senha)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (coop.get_razao(), coop.get_cnpj(), coop.get_email(), coop.get_endereco(), coop.get_fone(), coop.get_senha()))
        conn.commit()
        conn.close()

    @staticmethod
    def verificar_email(email):
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM cooperativa WHERE email = ?", (email,))
        dado = cursor.fetchone()
        conn.close()
        return dado is not None

    @staticmethod
    def verificar_cnpj(cnpj):
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM cooperativa WHERE cnpj = ?", (cnpj,))
        dado = cursor.fetchone()
        conn.close()
        return dado is not None

    @staticmethod
    def login(email, senha):
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM cooperativa WHERE email=?
        """, (email,))
        dado = cursor.fetchone()
        conn.close()

        if dado:
            coop = cooperativa(dado[0], dado[1], dado[2], dado[3], dado[4], dado[5], dado[6])
            if coop.get_senha() == senha:
                return coop
            else:
                raise ValueError("Senha incorreta")
        else:
            raise ValueError("Conta inexistente")

    @staticmethod
    def listar():
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cooperativa")
        dados = cursor.fetchall()
        conn.close()

        return [cooperativa(d[0], d[1], d[2], d[3], d[4], d[5], d[6]) for d in dados]

    @staticmethod
    def buscar_por_id(id):
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cooperativa WHERE id=?", (id,))
        dado = cursor.fetchone()
        conn.close()

        if dado:
            return cooperativa(dado[0], dado[1], dado[2], dado[3], dado[4], dado[5], dado[6])
        return None

    @staticmethod
    def atualizar(coop):
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE cooperativa SET razao_social=?, cnpj=?, email=?, endereco=?, fone=?, senha=?
            WHERE id=?
        """, (coop.get_razao(), coop.get_cnpj(), coop.get_email(), coop.get_endereco(), coop.get_fone(), coop.get_senha(), coop.get_id()))
        conn.commit()
        conn.close()

    @staticmethod
    def deletar(id):
        conn = BaseDAO.abrir()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cooperativa WHERE id=?", (id,))
        conn.commit()
        conn.close()
