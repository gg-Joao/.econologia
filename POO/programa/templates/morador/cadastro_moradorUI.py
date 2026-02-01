import streamlit as st
from models.morador import Morador
from dao.morador_dao import MoradorDAO
from utils.validacao_util import ValidacaoUtil
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
            if not nome or not email or not fone or not senha:
                st.error("Por favor, preencha todos os campos")
            elif "@" not in email or not email.endswith(".com") or email.count("@") != 1:
                st.error("Email inválido (formato: usuario@dominio.com)")
            elif len(senha) < 6:
                st.error("A senha deve ter no mínimo 6 caracteres")
            else:
                try:
                    morador = Morador(id, nome=nome, email=email, fone=fone, senha=senha)
                    MoradorDAO.inserir(morador)
                    st.success("Morador cadastrado com sucesso!")
                except ValueError as e:
                    st.error(str(e))
