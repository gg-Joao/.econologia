import streamlit as st
from dao.morador_dao import MoradorDAO
from models.morador import Morador

class PerfilMoradorUI:
    @staticmethod
    def main():
        st.header("Meu Perfil")      
        morador = MoradorDAO.buscar_por_id(st.session_state.usuario_id)
        
        if morador:
            st.subheader("Dados Pessoais")
            
            col1, col2 = st.columns(2)
            
            with col1:
                nome = st.text_input("Nome", value=morador.get_nome())
                email = st.text_input("Email", value=morador.get_email())
            
            with col2:
                fone = st.text_input("Telefone", value=morador.get_fone())
                pontos = st.number_input("Pontos", value=morador.get_pontos(), disabled=True)
            
            st.divider()
            st.subheader("Mudar Senha")
            
            senha_atual = st.text_input("Senha Atual", type="password")
            senha_nova = st.text_input("Nova Senha", type="password")
            confirmar_senha = st.text_input("Confirmar Senha", type="password")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button("Salvar"):
                    if morador.get_senha() == senha_atual or senha_atual == "":
                        morador.set_nome(nome)
                        if senha_nova and senha_nova == confirmar_senha:
                            morador.set_senha(senha_nova)
                        MoradorDAO.atualizar(morador)
                        st.success("Perfil atualizado!")
                    else:
                        st.error("Senha incorreta!")
            
            with col2:
                if st.button("Limpar"):
                    st.rerun()
            
            with col3:
                if st.button("Cancelar"):
                    st.session_state.tela = "painel_morador"
                    st.rerun()
