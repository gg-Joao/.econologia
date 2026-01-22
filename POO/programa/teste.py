from database import Database
from models.morador import Morador
from models.coleta import Coleta
from dao.morador_dao import MoradorDAO
from dao.coleta_dao import ColetaDAO
from datetime import datetime
import sqlite3

Database.criar_tabelas()
conn = sqlite3.connect('sistema.db')
cursor = conn.cursor()

id = cursor.lastrowid
# c = Coleta(id, data=datetime(2025, 12, 31), confirmado=False, descricao="auuu", pontos=20)
# ColetaDAO.inserir(c)
# m = Morador(id, "André", "isaque@email", 123, 10, "1234")
# MoradorDAO.inserir(m)

lista = MoradorDAO.listar()
for item in lista:
    print(item)
