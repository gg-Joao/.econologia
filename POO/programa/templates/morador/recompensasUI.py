import streamlit as st
from dao.recompensa_dao import RecompensaDAO
from dao.solicitacao_recompensa_dao import SolicitacaoRecompensaDAO
from dao.morador_dao import MoradorDAO
from models.solicitacao_recompensa import SolicitacaoRecompensa
from datetime import datetime
from utils.data_util import DataUtil

class RecompensasUI:
    @staticmethod
    def main():
        st.header("Recompensas")
        
        morador = MoradorDAO.buscar_por_id(st.session_state.usuario_id)
        pontos_atuais = morador.get_pontos() if morador else 0
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Seus Pontos", pontos_atuais)
        
        st.divider()

        recompensas = RecompensaDAO.listar()
        
        st.subheader("Disponíveis")
        
        if recompensas:
            for recompensa in recompensas:
                with st.container():
                    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
                    
                    with col1:
                        st.write(f"**{recompensa.get_nome()}**")
                        st.write(f"{recompensa.get_descricao()}")
                        st.write(f"Tipo: {recompensa.get_tipoRecompensa()}")
                        st.write(f"Válida até: {recompensa.get_validade()}")
                    
                    with col2:
                        st.metric("Pontos", recompensa.get_pontos())
                    
                    with col3:
                        faltam = recompensa.get_pontos() - pontos_atuais
                        if faltam > 0:
                            st.warning(f"Faltam {faltam}")
                        else:
                            st.success("Pronto!")
                    
                    with col3:
                        pontos_necessarios = recompensa.get_pontos()
                        if pontos_atuais >= pontos_necessarios:
                            if st.button("Resgatar", key=f"resgatar_{recompensa.get_id()}"):
                                novo_saldo = pontos_atuais - pontos_necessarios
                                morador.set_pontos(novo_saldo)
                                MoradorDAO.atualizar(morador)
                                
                                solicitacao = SolicitacaoRecompensa(
                                    morador_id=st.session_state.usuario_id,
                                    recompensa_id=recompensa.get_id(),
                                    data=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                    status="pendente"
                                )
                                SolicitacaoRecompensaDAO.inserir(solicitacao)
                                st.success("Solicitado!")
                                st.rerun()
                        else:
                            st.button("Indisponível", disabled=True, key=f"indisponivel_{recompensa.get_id()}")
                    
                    st.divider()
        else:
            st.info("Nenhuma recompensa no momento.")
        
        st.subheader("Minhas Solicitações")
        solicitacoes = SolicitacaoRecompensaDAO.listar_por_morador(st.session_state.usuario_id)
        
        if solicitacoes:
            for solicitacao in solicitacoes:
                recompensa = RecompensaDAO.buscar_por_id(solicitacao.get_recompensa_id())
                if recompensa:
                    status = solicitacao.get_status()
                    if status == "aprovada":
                        status_icon = "Aprovada"
                    elif status == "pendente":
                        status_icon = "Pendente"
                    else:
                        status_icon = "Rejeitada"
                    
                    with st.container():
                        st.write(f"**{recompensa.get_nome()}** - {status_icon}")
                        st.write(f"Data: {DataUtil.formatar_data_hora(solicitacao.get_data())}")
                        st.divider()
