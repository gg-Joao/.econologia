import sqlite3

class Database:
    @staticmethod
    def conectar():
        return sqlite3.connect("sistema.db", check_same_thread=False)

    @staticmethod
    def criar_tabelas():
        conn = Database.conectar()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS admin (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT UNIQUE,
            senha TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS morador (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            fone TEXT,
            pontos INTEGER,
            senha TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS coleta (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            confirmado INTEGER,
            descricao TEXT,
            pontos INTEGER
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS pontocoleta (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            endereco TEXT,
            telefone TEXT,
            horario TEXT,
            tipo TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS recompensa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            descricao TEXT,
            pontosnecessarios INTEGER,
            tiporecompensa TEXT,
            validade TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS solicitacao_recompensa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            morador_id INTEGER,
            recompensa_id INTEGER,
            data TEXT,
            status TEXT,
            FOREIGN KEY(morador_id) REFERENCES morador(id),
            FOREIGN KEY(recompensa_id) REFERENCES recompensa(id)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS cooperativa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            razao_social TEXT,
            cnpj TEXT UNIQUE,
            email TEXT UNIQUE,
            endereco TEXT,
            fone TEXT,
            senha TEXT
        )
        """)

