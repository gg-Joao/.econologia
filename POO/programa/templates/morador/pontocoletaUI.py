import streamlit as st
from dao.pontocoleta_dao import PontoColetaDAO

class PontoColetaUI:
    @staticmethod
    def main():
        st.header("Pontos de Coleta")
        
        pontos = PontoColetaDAO.listar()
        
        if pontos:
            st.subheader(f"Total: {len(pontos)} ponto(s)")
            
            for ponto in pontos:
                with st.container():
                    col1, col2 = st.columns([3, 1])
                    
                    with col1:
                        st.write(f"**{ponto.get_nome()}**")
                        st.write(f"{ponto.get_endereco()}")
                        st.write(f"{ponto.get_telefone()}")
                        st.write(f"{ponto.get_horario()}")
                    
                    with col2:
                        if st.button("Agendar", key=f"agendar_{ponto.get_id()}"):
                            st.session_state.ponto_coleta_id = ponto.get_id()
                            st.session_state.tela = "agendar_coleta"
                            st.rerun()
                    
                    st.divider()
        else:
            st.warning("Nenhum ponto de coleta disponível.")
