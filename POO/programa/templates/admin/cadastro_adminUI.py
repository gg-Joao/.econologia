import streamlit as st
from models.admin import Admin
from dao.admin_dao import AdminDAO

class CadastroAdminUI:
    @staticmethod
    def main():
        st.header("Abrir conta de Admin")
        
        if st.session_state.tipo_usuario != "admin":
            st.error("Apenas administradores já cadastrados podem criar novos administradores!")
            st.info("Faça login como administrador para abrir uma conta de novo admin.")
            return
        
        with st.form("cadastro_admin_form"):
            nome = st.text_input("Nome Completo")
            email = st.text_input("Email")
            senha = st.text_input("Senha", type="password")
            confirmar_senha = st.text_input("Confirmar Senha", type="password")
            
            cadastrar = st.form_submit_button("Abrir conta")
            
            if cadastrar:
                if nome and email and senha:
                    if "@" not in email or not email.endswith(".com") or email.count("@") != 1:
                        st.error("Email inválido (formato: usuario@dominio.com)")
                    elif len(senha) < 6:
                        st.error("A senha deve ter no mínimo 6 caracteres")
                    elif senha == confirmar_senha:
                        admins = AdminDAO.listar()
                        email_existe = any(a.get_email() == email for a in admins) if admins else False
                        
                        if not email_existe:
                            admin = Admin(nome=nome, email=email, senha=senha)
                            AdminDAO.inserir(admin)
                            st.success(" Administrador cadastrado com sucesso!")
                        else:
                            st.error("Este email já está cadastrado!")
                    else:
                        st.error("As senhas não correspondem!")
                else:
                    st.error("Preencha todos os campos!")
