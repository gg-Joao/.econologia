import streamlit as st
from dao.cooperativa_dao import CooperativaDAO
from dao.coleta_dao import ColetaDAO
from dao.morador_dao import MoradorDAO
from dao.recompensa_dao import RecompensaDAO
from dao.solicitacao_recompensa_dao import SolicitacaoRecompensaDAO
from utils.data_util import DataUtil

class PainelCooperativaUI:

    @staticmethod
    def dashboard():
        st.header("Painel")
        st.subheader(f"Bem-vindo, {st.session_state.usuario_nome}!")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            total_coletas = len(ColetaDAO.listar())
            st.metric("Coletas", total_coletas)
        
        with col2:
            total_moradores = len(MoradorDAO.listar())
            st.metric("Moradores", total_moradores)
        
        with col3:
            total_recompensas = len(RecompensaDAO.listar())
            st.metric("Recompensas", total_recompensas)

    @staticmethod
    def confirmar_resgate():
        """Confirmar resgate de recompensas"""
        st.header("Recompensas - Confirmar")
        
        solicitacoes = SolicitacaoRecompensaDAO.listar()
        
        if not solicitacoes:
            st.info("Nenhuma solicitação")
            return
        
        solicitacoes_pendentes = [s for s in solicitacoes if s.get_status() == "pendente"]
        
        if not solicitacoes_pendentes:
            st.info("Nenhuma solicitação pendente")
            return
        
        for sol in solicitacoes_pendentes:
            col1, col2, col3 = st.columns([2, 2, 1])
            
            morador = MoradorDAO.buscar_por_id(sol.get_morador_id())
            recompensa = RecompensaDAO.buscar_por_id(sol.get_recompensa_id())
            
            with col1:
                st.write(f"**Morador:** {morador.get_nome() if morador else 'N/A'}")
                st.write(f"**Recompensa:** {recompensa.get_nome() if recompensa else 'N/A'}")
            
            with col2:
                st.write(f"**Data:** {DataUtil.formatar_data_hora(sol.get_data())}")
                st.write(f"**Status:** {sol.get_status()}")
            
            with col3:
                if st.button("Confirmar", key=f"confirmar_{sol.get_id()}"):
                    sol.set_status("confirmado")
                    SolicitacaoRecompensaDAO.atualizar(sol)
                    st.success("Confirmado!")
                    st.rerun()

    @staticmethod
    def confirmar_agendamento():
        """Confirmar agendamento de coletas"""
        st.header("Coletas - Confirmar")
        
        coletas = ColetaDAO.listar()
        
        if not coletas:
            st.info("Nenhuma coleta")
            return
            coletas_nao_confirmadas = [c for c in coletas if c.get_confirmado() == 0]
        
        if not coletas_nao_confirmadas:
            st.info("Todas as coletas já foram confirmadas")
            return
        
        for coleta in coletas_nao_confirmadas:
            col1, col2, col3 = st.columns([2, 2, 1])
            
            with col1:
                st.write(f"**Data:** {DataUtil.formatar_data(coleta.get_data())}")
                st.write(f"**O quê:** {coleta.get_descricao()}")
            
            with col2:
                st.write(f"**Pontos:** {coleta.get_pontos()}")
                st.write(f"**Status:** {'Sim' if coleta.get_confirmado() else 'Não'}")
            
            with col3:
                if st.button("Confirmar", key=f"confirmar_coleta_{coleta.get_id()}"):
                    coleta.set_confirmado(1)
                    ColetaDAO.atualizar(coleta)
                    st.success("Confirmado!")
                    st.rerun()

    @staticmethod
    def visualizar_coletas():
        """Funcionalidade: Visualizar Coletas"""
        st.header("Visualizar Coletas")
        
        coletas = ColetaDAO.listar()
        
        if not coletas:
            st.info("Nenhuma coleta registrada")
            return
        
        for coleta in coletas:
            with st.container():
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.write(f"**ID:** {coleta.get_id()}")
                    st.write(f"**Data:** {DataUtil.formatar_data(coleta.get_data())}")
                    st.write(f"**Descrição:** {coleta.get_descricao()}")
                    st.write(f"**Pontos:** {coleta.get_pontos()}")
                    st.write(f"**Confirmado:** {'✓ Sim' if coleta.get_confirmado() else '✗ Não'}")
                
                with col2:
                    if st.button("Editar", key=f"editar_coleta_{coleta.get_id()}"):
                        st.session_state.coleta_selecionada = coleta.get_id()
                
                st.divider()

    @staticmethod
    def visualizar_residuos():
        """Funcionalidade: Visualizar Resíduos coletados"""
        st.header("Visualizar Resíduos Coletados")
        
        coletas = ColetaDAO.listar()
        
        if not coletas:
            st.info("Nenhuma coleta de resíduos registrada")
            return
        
        st.subheader("Resumo de Coletas de Resíduos")
        
        total_pontos = sum(c.get_pontos() for c in coletas)
        total_coletas = len(coletas)
        coletas_confirmadas = len([c for c in coletas if c.get_confirmado() == 1])
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total de Coletas", total_coletas)
        with col2:
            st.metric("Coletas Confirmadas", coletas_confirmadas)
        with col3:
            st.metric("Total de Pontos", total_pontos)
        
        st.subheader("Detalhes das Coletas")
        for coleta in coletas:
            st.write(f"**ID:** {coleta.get_id()} | **Data:** {coleta.get_data()} | **Descrição:** {coleta.get_descricao()} | **Pontos:** {coleta.get_pontos()}")

    @staticmethod
    def main():
        """Painel principal da cooperativa"""
        opcao = st.session_state.tela
        
        if opcao == "painel_cooperativa":
            PainelCooperativaUI.dashboard()
        elif opcao == "confirmar_resgate":
            PainelCooperativaUI.confirmar_resgate()
        elif opcao == "confirmar_agendamento":
            PainelCooperativaUI.confirmar_agendamento()
        elif opcao == "visualizar_coletas":
            PainelCooperativaUI.visualizar_coletas()
        elif opcao == "visualizar_residuos":
            PainelCooperativaUI.visualizar_residuos()
        else:
            PainelCooperativaUI.dashboard()
