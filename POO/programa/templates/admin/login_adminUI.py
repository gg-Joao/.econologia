import streamlit as st
from dao.admin_dao import AdminDAO

class LoginAdminUI:
    @staticmethod
    def main():
        st.header("Login do Administrador")

        with st.form("login_admin"):
            email = st.text_input("Email")
            senha = st.text_input("Senha", type="password")

            entrar = st.form_submit_button("Entrar")

            if entrar:
                admin = AdminDAO.login(email, senha)
                if admin:
                    st.session_state.usuario_id = admin.get_id()
                    st.session_state.usuario_nome = admin.get_nome()
                    st.session_state.tipo_usuario = "admin"
                    st.session_state.tela = "painel_admin"
                    st.rerun()
                else:
                    st.error("Email ou senha inválidos")