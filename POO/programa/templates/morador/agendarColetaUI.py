import streamlit as st
from datetime import datetime
from dao.coleta_dao import ColetaDAO
from dao.pontocoleta_dao import PontoColetaDAO
from models.coleta import Coleta

class AgendarColetaUI:
    @staticmethod
    def main():
        st.header("Agendar Coleta")
        
        pontos = PontoColetaDAO.listar()
        
        if not pontos:
            st.error("Nenhum ponto de coleta disponível.")
            return
        
        opcoes_pontos = {ponto.get_nome(): ponto.get_id() for ponto in pontos}
        
        with st.form("agendar_coleta_form"):
            ponto_selecionado = st.selectbox("Escolha o local", list(opcoes_pontos.keys()))
            data_coleta = st.date_input("Data")
            descricao = st.text_area("Materiais a coletar", placeholder="Ex: 2kg de papel, 1kg de plástico...")
            
            agendar = st.form_submit_button("Agendar")
            
            if agendar:
                if not descricao.strip():
                    st.error("Descreva os materiais.")
                elif data_coleta < datetime.today().date():
                    st.error("A data não pode ser no passado.")
                else:
                    coleta = Coleta(
                        data=str(data_coleta),
                        descricao=descricao,
                        confirmado=0
                    )
                    ColetaDAO.inserir(coleta)
                    st.success("Coleta agendada!")
                    st.session_state.tela = "minhas_coletas"
                    st.rerun()
