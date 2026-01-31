import streamlit as st
from dao.cooperativa_dao import CooperativaDAO
from models.cooperativa import cooperativa
from utils.validacao_util import ValidacaoUtil

class CadastroCooperativaUI:
    @staticmethod
    def main():
        st.header("Cadastro de Cooperativa")

        with st.form("cadastro_cooperativa"):
            razao = st.text_input("Razão Social (3-100 caracteres)")
            cnpj = st.text_input("CNPJ (14 dígitos)")
            email = st.text_input("Email (5-100 caracteres)")
            endereco = st.text_area("Endereço (5-200 caracteres)")
            fone = st.text_input("Telefone (10-11 dígitos)")
            senha = st.text_input("Senha (6-20 caracteres)", type="password")
            confirmar_senha = st.text_input("Confirmar Senha", type="password")

            cadastrar = st.form_submit_button("Cadastrar")

            if cadastrar:
                if not cnpj or not email or not endereco or not fone or not senha:
                    st.error("Por favor, preencha todos os campos")
                elif "@" not in email or not email.endswith(".com") or email.count("@") != 1:
                    st.error("Email inválido (formato: usuario@dominio.com)")
                elif senha != confirmar_senha:
                    st.error("As senhas não coincidem")
                elif len(senha) < 6:
                    st.error("A senha deve ter no mínimo 6 caracteres")
                else:
                    try:
                        nova_cooperativa = cooperativa(
                            cnpj=cnpj,
                            razaoSocial=razao,
                            email=email,
                            endereco=endereco,
                            fone=fone,
                            senha=senha
                        )
                        CooperativaDAO.inserir(nova_cooperativa)
                        st.success("Cooperativa cadastrada com sucesso! Faça login para continuar.")
                    except ValueError as e:
                        st.error(str(e))
                    except Exception as e:
                        st.error(f"Erro ao cadastrar: {str(e)}")
