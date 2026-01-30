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
<<<<<<< HEAD
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
=======
        
        with st.form("cadastro_morador"):
            nome = st.text_input("Nome (3-50 caracteres)")
            email = st.text_input("Email (5-100 caracteres)")
            fone = st.text_input("Telefone (10-11 dígitos)")
            senha = st.text_input("Senha (6-20 caracteres)", type="password")
            confirmar_senha = st.text_input("Confirmar Senha", type="password")
            
            cadastrar = st.form_submit_button("Cadastrar")
            if cadastrar:
                valido, msg = ValidacaoUtil.validar_nome(nome)
                if not valido:
                    st.error(f"Nome: {msg}")
                    return
                
                valido, msg = ValidacaoUtil.validar_email(email)
                if not valido:
                    st.error(f"Email: {msg}")
                    return
                        
                valido, msg = ValidacaoUtil.validar_telefone(fone)
                if not valido:
                    st.error(f"Telefone: {msg}")
                    return
                         
                valido, msg = ValidacaoUtil.validar_senha(senha)
                if not valido:
                    st.error(f"Senha: {msg}")
                    return
                
         
                if senha != confirmar_senha:
                    st.error("As senhas não coincidem")
                    return       
                try:
                    morador = Morador(id, nome=nome, email=email, fone=fone, senha=senha)
                    MoradorDAO.inserir(morador)
                    st.success(" Morador cadastrado com sucesso!")
                except Exception as e:
                    st.error(f" Erro ao cadastrar: {str(e)}")
                finally:
                    conn.close()
>>>>>>> 7dae6e3a481acd4b5ae2aa14c27fc8d091f7ca61
