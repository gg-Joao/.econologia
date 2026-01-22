import streamlit as st
from dao.coleta_dao import ColetaDAO
from utils.data_util import DataUtil

class MinhasColetasUI:
    @staticmethod
    def main():
        st.header("Minhas Coletas")
        coletas = ColetaDAO.listar()
        if coletas:
            
            confirmadas = [c for c in coletas if c.get_confirmado()]
            pendentes = [c for c in coletas if not c.get_confirmado()]
        
            st.subheader(f"Confirmadas ({len(confirmadas)})")
            if confirmadas:
                for coleta in confirmadas:
                    with st.container():
                        st.write(f"**Data:** {DataUtil.formatar_data(coleta.get_data())}")
                        st.write(f"**O quê:** {coleta.get_descricao()}")
                        st.write(f"**Pontos:** +{coleta.get_pontos()}")
                        st.success("Confirmada")
                        st.divider()
            else:
                st.info("Nenhuma coleta confirmada.")
        
            st.subheader(f"Pendentes ({len(pendentes)})")
            if pendentes:
                for coleta in pendentes:
                    with st.container():
                        st.write(f"**Data:** {DataUtil.formatar_data(coleta.get_data())}")
                        st.write(f"**O quê:** {coleta.get_descricao()}")
                        st.warning("Aguardando confirmação")
                        st.divider()
            else:
                st.info("Nenhuma coleta pendente.")
        else:
            st.info("Você ainda não agendou coletas.")
