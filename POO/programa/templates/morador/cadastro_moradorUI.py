import streamlit as st
from models.morador import Morador
from dao.morador_dao import MoradorDAO
import sqlite3

class CadastroMoradorUI:
    @staticmethod
    def main():
        conn = sqlite3.connect('sistema.db')
        cursor = conn.cursor()
        st.header("Cadastro de Morador")
        id = cursor.lastrowid
        nome = st.text_input("Nome")
        email = st.text_input("Email")
        fone = st.text_input("Telefone")
        senha = st.text_input("Senha", type="password")

        if st.button("Cadastrar"):
            morador = Morador(id, nome=nome, email=email, fone=fone, senha=senha)
            MoradorDAO.inserir(morador)
            st.success("Morador cadastrado com sucesso!")