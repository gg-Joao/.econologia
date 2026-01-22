import streamlit as st
from dao.cooperativa_dao import CooperativaDAO

class LoginCooperativaUI:
    @staticmethod
    def main():
        st.header("Login da Cooperativa")

        with st.form("login_cooperativa"):
            email = st.text_input("Email")
            senha = st.text_input("Senha", type="password")

            entrar = st.form_submit_button("Entrar")

            if entrar:
                cooperativa = CooperativaDAO.login(email, senha)
                if cooperativa:
                    st.session_state.usuario_id = cooperativa.get_id()
                    st.session_state.usuario_nome = cooperativa.get_razao()
                    st.session_state.tipo_usuario = "cooperativa"
                    st.session_state.tela = "painel_cooperativa"
                    st.rerun()
                else:
                    st.error("Email ou senha inválidos")
