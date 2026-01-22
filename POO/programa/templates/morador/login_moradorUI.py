import streamlit as st
from dao.morador_dao import MoradorDAO

class LoginMoradorUI:

    @staticmethod
    def main():
        st.header(" Login do Morador")

        with st.form("login_morador"):
            email = st.text_input("Email")
            senha = st.text_input("Senha", type="password")

            entrar = st.form_submit_button("Entrar")

            if entrar:
                morador = MoradorDAO.login(email, senha)
                if morador:
                    st.session_state.usuario_id = morador.get_id()
                    st.session_state.usuario_nome = morador.get_nome()
                    st.session_state.tipo_usuario = "morador"
                    st.session_state.tela = "painel_morador"
                    st.rerun()
                else:
                    st.error("Email ou senha inválidos")
