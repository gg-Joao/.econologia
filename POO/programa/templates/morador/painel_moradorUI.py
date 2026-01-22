import streamlit as st
from dao.morador_dao import MoradorDAO

class PainelMoradorUI:
    @staticmethod
    def main():
        st.header("Meu Painel")
        
        morador = MoradorDAO.buscar_por_id(st.session_state.usuario_id)
        
        if morador:
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Pontos", morador.get_pontos())
            
            with col2:
                st.metric("Nome", morador.get_nome())
            
            with col3:
                st.metric("Email", morador.get_email())
            
            st.divider()
            
            st.subheader("Bem-vindo!")
            st.info("Sistema de Coleta Seletiva")
            st.write(f"Olá, **{morador.get_nome()}**! Você tem **{morador.get_pontos()}** pontos.")
            
            st.subheader("O que fazer?")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button("Pontos de Coleta"):
                    st.session_state.tela = "pontos_coleta"
                    st.rerun()
            
            with col2:
                if st.button("Agendar Coleta"):
                    st.session_state.tela = "agendar_coleta"
                    st.rerun()

            with col3:
                if st.button("Recompensas"):
                    st.session_state.tela = "recompensas"
                    st.rerun()
