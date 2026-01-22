import streamlit as st
import sqlite3
from database import Database
from templates.morador.login_moradorUI import LoginMoradorUI
from templates.morador.cadastro_moradorUI import CadastroMoradorUI
from templates.morador.painel_moradorUI import PainelMoradorUI
from templates.morador.pontocoletaUI import PontoColetaUI
from templates.morador.agendarColetaUI import AgendarColetaUI
from templates.morador.minhasColetasUI import MinhasColetasUI
from templates.morador.recompensasUI import RecompensasUI
from templates.morador.perfilMoradorUI import PerfilMoradorUI
from templates.admin.login_adminUI import LoginAdminUI
from templates.admin.cadastro_adminUI import CadastroAdminUI
from templates.admin.painel_adminUI import PainelAdminUI
from templates.cooperativa.login_cooperativaUI import LoginCooperativaUI
from templates.cooperativa.cadastro_cooperativaUI import CadastroCooperativaUI
from templates.cooperativa.painel_cooperativaUI import PainelCooperativaUI


def reiniciar_app():
    try:
        st.experimental_rerun()
    except AttributeError:
        try:
            st.rerun()
        except Exception as e:
            st.error(f"Erro ao reiniciar o app: {e}")


class IndexUI:

    @staticmethod
    def main():
        Database.criar_tabelas()
        IndexUI.inicializar_sessao()
        st.title("Sistema de Coleta Seletiva")
        IndexUI.sidebar()
        IndexUI.renderizar_pagina()

    @staticmethod
    def inicializar_sessao():
        if "usuario_id" not in st.session_state:
            st.session_state.usuario_id = None

        if "usuario_nome" not in st.session_state:
            st.session_state.usuario_nome = None

        if "tipo_usuario" not in st.session_state:
            st.session_state.tipo_usuario = None  # visitante | morador | admin
        
        if "tela" not in st.session_state:
            st.session_state.tela = None
    @staticmethod
    def menu_visitante():
        op = st.sidebar.selectbox(
            "Menu",
            ["Login Morador", "Abrir conta de Morador", "Login Admin", "Login Cooperativa", "Abrir conta de Cooperativa"]
        )

        if op == "Login Morador":
            LoginMoradorUI.main()

        if op == "Abrir conta de Morador":
            CadastroMoradorUI.main()

        if op == "Login Admin":
            LoginAdminUI.main()

        if op == "Login Cooperativa":
            LoginCooperativaUI.main()

        if op == "Abrir conta de Cooperativa":
            CadastroCooperativaUI.main()

    @staticmethod
    def menu_morador():
        st.sidebar.subheader("Menu do Morador")

        if st.sidebar.button("Painel Inicial"):
            st.session_state.tela = "painel_morador"

        if st.sidebar.button("Pontos de Coleta"):
            st.session_state.tela = "pontos_coleta"

        if st.sidebar.button("Agendar Coleta"):
            st.session_state.tela = "agendar_coleta"

        if st.sidebar.button("Minhas Coletas"):
            st.session_state.tela = "minhas_coletas"

        if st.sidebar.button("Recompensas"):
            st.session_state.tela = "recompensas"

        if st.sidebar.button(" Meu Perfil"):
            st.session_state.tela = "perfil_morador"

    @staticmethod
    def menu_cooperativa():
        st.sidebar.subheader(f"Menu da Cooperativa")
        st.sidebar.write(f"Cooperativa: {st.session_state.usuario_nome}")
        
        if st.sidebar.button("Dashboard"):
            st.session_state.tela = "painel_cooperativa"
            st.rerun()
        
        if st.sidebar.button("Confirmar Resgate"):
            st.session_state.tela = "confirmar_resgate"
            st.rerun()
        
        if st.sidebar.button("Confirmar Agendamento"):
            st.session_state.tela = "confirmar_agendamento"
            st.rerun()
        
        if st.sidebar.button("Visualizar Coletas"):
            st.session_state.tela = "visualizar_coletas"
            st.rerun()
        
        if st.sidebar.button("Visualizar Resíduos"):
            st.session_state.tela = "visualizar_residuos"
            st.rerun()


    @staticmethod
    def menu_admin():
        st.sidebar.write(f"Admin: {st.session_state.usuario_nome}")
        
        if st.sidebar.button("Dashboard"):
            st.session_state.tela = "dashboard_admin"
            st.rerun()
        
        if st.sidebar.button("Gerenciar Moradores"):
            st.session_state.tela = "gerenciar_moradores"
            st.rerun()
        
        if st.sidebar.button("Gerenciar Coletas"):
            st.session_state.tela = "gerenciar_coletas"
            st.rerun()
        
        if st.sidebar.button("Gerenciar Pontos de Coleta"):
            st.session_state.tela = "gerenciar_pontos_coleta"
            st.rerun()
        
        if st.sidebar.button("Gerenciar Recompensas"):
            st.session_state.tela = "gerenciar_recompensas"
            st.rerun()
        
        if st.sidebar.button("Solicitações"):
            st.session_state.tela = "gerenciar_solicitacoes_recompensa"
            st.rerun()
        
        if st.sidebar.button("Abrir conta de Admin"):
            st.session_state.tela = "abrir_conta_admin"
            st.rerun()

    @staticmethod
    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            st.session_state.usuario_id = None
            st.session_state.usuario_nome = None
            st.session_state.tipo_usuario = None
            reiniciar_app()

    @staticmethod
    def sidebar():
        if st.session_state.usuario_id is None:
            IndexUI.menu_visitante()
        else:
            if st.session_state.tipo_usuario == "admin":
                IndexUI.menu_admin()
            elif st.session_state.tipo_usuario == "morador":
                IndexUI.menu_morador()
            elif st.session_state.tipo_usuario == "cooperativa":
                IndexUI.menu_cooperativa()

            IndexUI.sair_do_sistema()

    @staticmethod
    def renderizar_pagina():
        """Renderiza a página baseado no estado 'tela'"""
        if st.session_state.tipo_usuario == "morador":
            if st.session_state.tela == "painel_morador":
                PainelMoradorUI.main()
            elif st.session_state.tela == "pontos_coleta":
                PontoColetaUI.main()
            elif st.session_state.tela == "agendar_coleta":
                AgendarColetaUI.main()
            elif st.session_state.tela == "minhas_coletas":
                MinhasColetasUI.main()
            elif st.session_state.tela == "recompensas":
                RecompensasUI.main()
            elif st.session_state.tela == "perfil_morador":
                PerfilMoradorUI.main()
            else:
                PainelMoradorUI.main()
        elif st.session_state.tipo_usuario == "admin":
            if st.session_state.tela == "dashboard_admin":
                PainelAdminUI.dashboard()
            elif st.session_state.tela == "gerenciar_moradores":
                PainelAdminUI.gerenciar_moradores()
            elif st.session_state.tela == "gerenciar_coletas":
                PainelAdminUI.gerenciar_coletas()
            elif st.session_state.tela == "gerenciar_pontos_coleta":
                PainelAdminUI.gerenciar_pontos_coleta()
            elif st.session_state.tela == "gerenciar_recompensas":
                PainelAdminUI.gerenciar_recompensas()
            elif st.session_state.tela == "gerenciar_solicitacoes_recompensa":
                PainelAdminUI.gerenciar_solicitacoes_recompensa()
            elif st.session_state.tela == "abrir_conta_admin":
                CadastroAdminUI.main()
            else:
                PainelAdminUI.dashboard()
        elif st.session_state.tipo_usuario == "cooperativa":
            if st.session_state.tela == "painel_cooperativa":
                PainelCooperativaUI.dashboard()
            elif st.session_state.tela == "confirmar_resgate":
                PainelCooperativaUI.confirmar_resgate()
            elif st.session_state.tela == "confirmar_agendamento":
                PainelCooperativaUI.confirmar_agendamento()
            elif st.session_state.tela == "visualizar_coletas":
                PainelCooperativaUI.visualizar_coletas()
            elif st.session_state.tela == "visualizar_residuos":
                PainelCooperativaUI.visualizar_residuos()
            else:
                PainelCooperativaUI.dashboard()

IndexUI.main()
