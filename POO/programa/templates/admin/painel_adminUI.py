import streamlit as st
from dao.admin_dao import AdminDAO
from dao.morador_dao import MoradorDAO
from dao.coleta_dao import ColetaDAO
from dao.recompensa_dao import RecompensaDAO
from dao.solicitacao_recompensa_dao import SolicitacaoRecompensaDAO
from dao.pontocoleta_dao import PontoColetaDAO
from dao.cooperativa_dao import CooperativaDAO
from utils.data_util import DataUtil

class PainelAdminUI:
    
    @staticmethod
    def dashboard():
        st.header("Painel")
        
        moradores = MoradorDAO.listar()
        coletas = ColetaDAO.listar()
        recompensas = RecompensaDAO.listar()
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Moradores", len(moradores) if moradores else 0)
        
        with col2:
            st.metric("Coletas", len(coletas) if coletas else 0)
        
        with col3:
            confirmadas = len([c for c in coletas if c.get_confirmado()]) if coletas else 0
            st.metric("Confirmadas", confirmadas)
        
        with col4:
            st.metric("Recompensas", len(recompensas) if recompensas else 0)
    
    @staticmethod
    def gerenciar_moradores():
        st.header("Moradores")
        
        tab1, tab2 = st.tabs(["Ver", "Editar"])
        
        with tab1:
            moradores = MoradorDAO.listar()
            
            if moradores:
                dados = []
                for m in moradores:
                    dados.append({
                        "ID": m.get_id(),
                        "Nome": m.get_nome(),
                        "Email": m.get_email(),
                        "Telefone": m.get_fone(),
                        "Pontos": m.get_pontos()
                    })
                
                st.dataframe(dados, use_container_width=True)
            else:
                st.info("Nenhum morador cadastrado.")
        
        with tab2:
            moradores = MoradorDAO.listar()
            
            if moradores:
                st.subheader("Escolha um morador")
                
                opcoes = [f"{m.get_id()} - {m.get_nome()}" for m in moradores]
                morador_selecionado = st.selectbox("Morador:", opcoes)
                
                morador_id = int(morador_selecionado.split(" - ")[0])
                morador = MoradorDAO.buscar_por_id(morador_id)
                
                if morador:
                    st.divider()
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.subheader("Editar")
                        with st.form(f"form_editar_morador_{morador_id}"):
                            nome = st.text_input("Nome", value=morador.get_nome())
                            email = st.text_input("Email", value=morador.get_email())
                            fone = st.text_input("Telefone", value=morador.get_fone())
                            pontos = st.number_input("Pontos", value=morador.get_pontos(), min_value=0)
                            
                            if st.form_submit_button("Salvar"):
                                morador.set_nome(nome)
                                morador.set_email(email)
                                morador.set_fone(fone)
                                morador.set_pontos(pontos)
                                
                                MoradorDAO.atualizar(morador)
                                st.success("Atualizado!")
                                st.rerun()
                    
                    with col2:
                        st.subheader("Ações")
                        st.write("**Dados:**")
                        st.write(f"ID: {morador.get_id()}")
                        st.write(f"Nome: {morador.get_nome()}")
                        st.write(f"Email: {morador.get_email()}")
                        st.write(f"Telefone: {morador.get_fone()}")
                        st.write(f"Pontos: {morador.get_pontos()}")
                        
                        st.divider()
                        
                        if st.button("Deletar", use_container_width=True):
                            MoradorDAO.deletar(morador_id)
                            st.success("Deletado!")
                            st.rerun()
            else:
                st.info("Nenhum morador cadastrado.")
    @staticmethod
    def gerenciar_coletas():
        st.header("Gerenciar Coletas")
        
        tab1, tab2 = st.tabs(["Coletas Pendentes", "Coletas Confirmadas"])
        
        coletas = ColetaDAO.listar()
        
        if coletas:
            pendentes = [c for c in coletas if not c.get_confirmado()]
            confirmadas = [c for c in coletas if c.get_confirmado()]
            
            with tab1:
                st.subheader(f"Coletas Pendentes de Confirmação ({len(pendentes)})")
                
                if pendentes:
                    for coleta in pendentes:
                        with st.container():
                            col1, col2, col3 = st.columns([3, 1, 1])
                            
                            with col1:
                                st.write(f"**ID:** {coleta.get_id()}")
                                st.write(f"**Data:** {DataUtil.formatar_data(coleta.get_data())}")
                                st.write(f"**Descrição:** {coleta.get_descricao()}")
                            
                            with col2:
                                if st.button("Confirmar", key=f"confirmar_{coleta.get_id()}", use_container_width=True):
                                    coleta.set_confirmado(1)
                                    coleta.set_pontos(10)  # Pontos padrão para coleta confirmada
                                    ColetaDAO.atualizar(coleta)
                                    st.success("Coleta confirmada!")
                                    st.rerun()
                            
                            with col3:
                                if st.button("Rejeitar", key=f"rejeitar_{coleta.get_id()}", use_container_width=True):
                                    ColetaDAO.deletar(coleta.get_id())
                                    st.warning("Coleta rejeitada!")
                                    st.rerun()
                            
                            st.divider()
                else:
                    st.info("Nenhuma coleta pendente de confirmação.")
            
            with tab2:
                st.subheader(f"Coletas Confirmadas ({len(confirmadas)})")
                
                if confirmadas:
                    opcoes = [f"{c.get_id()} - {DataUtil.formatar_data(c.get_data())} - {c.get_descricao()[:30]}" for c in confirmadas]
                    coleta_selecionada = st.selectbox("Selecione uma coleta para editar:", opcoes)
                    
                    coleta_id = int(coleta_selecionada.split(" - ")[0])
                    coleta = ColetaDAO.buscar_por_id(coleta_id)
                    
                    if coleta:
                        st.divider()
                        
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.subheader("Editar Coleta")
                            with st.form(f"form_editar_coleta_{coleta_id}"):
                                data = st.date_input("Data", value=coleta.get_data() if isinstance(coleta.get_data(), str) else coleta.get_data())
                                descricao = st.text_area("Descrição", value=coleta.get_descricao())
                                pontos = st.number_input("Pontos", value=coleta.get_pontos(), min_value=0, max_value=100)
                                
                                if st.form_submit_button("Salvar Alterações"):
                                    coleta.set_data(str(data))
                                    coleta.set_desc(descricao)
                                    coleta.set_pontos(pontos)
                                    ColetaDAO.atualizar(coleta)
                                    st.success("Coleta atualizada com sucesso!")
                                    st.rerun()
                        
                        with col2:
                            st.subheader("Informações")
                            st.write(f"**ID:** {coleta.get_id()}")
                            st.write(f"**Data:** {DataUtil.formatar_data(coleta.get_data())}")
                            st.write(f"**Descrição:** {coleta.get_descricao()}")
                            st.write(f"**Pontos:** {coleta.get_pontos()}")
                            
                            st.divider()
                            
                            if st.button("Deletar Coleta", use_container_width=True):
                                ColetaDAO.deletar(coleta_id)
                                st.success("Coleta deletada!")
                                st.rerun()
                else:
                    st.info("Nenhuma coleta confirmada.")
        else:
            st.info("Nenhuma coleta agendada.")
    
    @staticmethod
    def gerenciar_pontos_coleta():
        st.header("Gerenciar Pontos de Coleta")
        
        tab1, tab2 = st.tabs(["Listar Pontos", "Adicionar/Editar Ponto"])
        
        with tab1:
            pontos = PontoColetaDAO.listar()
            
            if pontos:
                dados = []
                for p in pontos:
                    dados.append({
                        "ID": p.get_id(),
                        "Nome": p.get_nome(),
                        "Endereço": p.get_endereco(),
                        "Telefone": p.get_telefone(),
                        "Horário": p.get_horario()
                    })
                
                st.dataframe(dados, use_container_width=True)
            else:
                st.info("Nenhum ponto de coleta cadastrado.")
        
        with tab2:
            st.subheader("Adicionar Novo Ponto de Coleta")
            
            with st.form("form_novo_ponto_coleta"):
                nome = st.text_input("Nome do Ponto")
                endereco = st.text_area("Endereço (Rua, Número, Bairro, Referência)")
                telefone = st.text_input("Telefone")
                
                col_inicio, col_fim = st.columns(2)
                with col_inicio:
                    horario_inicio = st.time_input("Horário de Início", value=None)
                with col_fim:
                    horario_fim = st.time_input("Horário de Fim", value=None)
                
                if st.form_submit_button("Adicionar Ponto"):
                    if nome and endereco and telefone and horario_inicio and horario_fim:
                        if horario_fim <= horario_inicio:
                            st.error("O horário de fim deve ser maior que o horário de início!")
                        else:
                            from models.pontocoleta import PontoColeta
                            horario_formatado = f"{horario_inicio.strftime('%H:%M')} - {horario_fim.strftime('%H:%M')}"
                            novo_ponto = PontoColeta(
                                nome=nome,
                                endereco=endereco,
                                fone=telefone,
                                funcionamento=horario_formatado
                            )
                            PontoColetaDAO.inserir(novo_ponto)
                            st.success("Ponto de coleta adicionado com sucesso!")
                            st.rerun()
                    else:
                        st.error("Preencha todos os campos!")
            
            st.divider()
            st.subheader("Editar ou Deletar Ponto de Coleta")
            
            pontos = PontoColetaDAO.listar()
            
            if pontos:
                opcoes = [f"{p.get_id()} - {p.get_nome()}" for p in pontos]
                ponto_selecionado = st.selectbox("Selecione um ponto:", opcoes)
                
                ponto_id = int(ponto_selecionado.split(" - ")[0])
                ponto = PontoColetaDAO.buscar_por_id(ponto_id)
                
                if ponto:
                    st.divider()
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.subheader("Editar Ponto")
                        with st.form(f"form_editar_ponto_{ponto_id}"):
                            nome = st.text_input("Nome", value=ponto.get_nome())
                            endereco = st.text_area("Endereço", value=ponto.get_endereco())
                            telefone = st.text_input("Telefone", value=ponto.get_telefone())
                            
                            horario_atual = ponto.get_horario()
                            if " - " in horario_atual:
                                partes = horario_atual.split(" - ")
                                try:
                                    from datetime import datetime
                                    hora_inicio = datetime.strptime(partes[0], "%H:%M").time()
                                    hora_fim = datetime.strptime(partes[1], "%H:%M").time()
                                except:
                                    hora_inicio = None
                                    hora_fim = None
                            else:
                                hora_inicio = None
                                hora_fim = None
                            
                            col_inicio, col_fim = st.columns(2)
                            with col_inicio:
                                horario_inicio = st.time_input("Horário de Início", value=hora_inicio)
                            with col_fim:
                                horario_fim = st.time_input("Horário de Fim", value=hora_fim)
                            
                            if st.form_submit_button("Salvar Alterações"):
                                if horario_fim <= horario_inicio:
                                    st.error("O horário de fim deve ser maior que o horário de início!")
                                else:
                                    horario_formatado = f"{horario_inicio.strftime('%H:%M')} - {horario_fim.strftime('%H:%M')}"
                                    ponto.set_nome(nome)
                                    ponto.set_endereco(endereco)
                                    ponto.set_fone(telefone)
                                    ponto.set_funcionamento(horario_formatado)
                                    
                                    PontoColetaDAO.atualizar(ponto)
                                    st.success("Ponto atualizado com sucesso!")
                                    st.rerun()
                    
                    with col2:
                        st.subheader("Informações")
                        st.write(f"**ID:** {ponto.get_id()}")
                        st.write(f"**Nome:** {ponto.get_nome()}")
                        st.write(f"**Endereço:** {ponto.get_endereco()}")
                        st.write(f"**Telefone:** {ponto.get_telefone()}")
                        st.write(f"**Horário:** {ponto.get_horario()}")
                        
                        st.divider()
                        
                        if st.button("Deletar Ponto", use_container_width=True):
                            PontoColetaDAO.deletar(ponto_id)
                            st.success("Ponto deletado!")
                            st.rerun()
            else:
                st.info("Nenhum ponto de coleta cadastrado.")
    
    @staticmethod
    def gerenciar_recompensas():
        st.header("Gerenciar Recompensas")
        recompensas = RecompensaDAO.listar()
        st.write("Adicionar Nova Recompensa:")
        with st.form("form_nova_recompensa"):
            nome = st.text_input("Nome da Recompensa")
            descricao = st.text_area("Descrição")
            pontos = st.number_input("Pontos Necessários", min_value=1, value=100)
            tipo_recompensa = st.selectbox("Tipo de Recompensa", ["Desconto", "Brinde", "Voucher", "Outro"])
            validade = st.date_input("Data de Validade")
            
            if st.form_submit_button("Adicionar Recompensa"):
                if nome and descricao:
                    from models.recompensa import Recompensa
                    nova_recompensa = Recompensa(
                        id=None,
                        nome=nome,
                        descricao=descricao,
                        pontosNecessarios=pontos,
                        tipoRecompensa=tipo_recompensa,
                        validade=DataUtil.formatar_data(str(validade))
                    )
                    RecompensaDAO.inserir(nova_recompensa)
                    st.success("Recompensa adicionada com sucesso!")
                    st.rerun()
                else:
                    st.error("Preencha todos os campos.")
        
        st.divider()
        st.write("**Recompensas Cadastradas:**")
        if recompensas:
            for recompensa in recompensas:
                with st.container():
                    col1, col2, col3 = st.columns([3, 1, 1])
                    
                    with col1:
                        st.write(f"**{recompensa.get_nome()}**")
                        st.write(f"Descrição: {recompensa.get_descricao()}")
                        st.write(f"Tipo: {recompensa.get_tipoRecompensa()}")
                        st.write(f"Válida até: {recompensa.get_validade()}")
                    
                    with col2:
                        st.write(f"**{recompensa.get_pontos()} pontos**")
                    
                    with col3:
                        if st.button("Deletar", key=f"deletar_{recompensa.get_id()}"):
                            RecompensaDAO.deletar(recompensa.get_id())
                            st.success("Recompensa removida!")
                            st.rerun()
                    
                    st.divider()
        else:
            st.info("Nenhuma recompensa cadastrada.")
    
    @staticmethod
    def gerenciar_solicitacoes_recompensa():
        st.header("Gerenciar Solicitacoes de Recompensa")
        
        solicitacoes = SolicitacaoRecompensaDAO.listar()
        
        if solicitacoes:
            pendentes = [s for s in solicitacoes if s.get_status() == "pendente"]
            aprovadas = [s for s in solicitacoes if s.get_status() == "aprovada"]
            st.write("**Solicitacoes Pendentes de Aprovacao:**")
            if pendentes:
                for solicitacao in pendentes:
                    morador = MoradorDAO.buscar_por_id(solicitacao.get_morador_id())
                    recompensa = RecompensaDAO.buscar_por_id(solicitacao.get_recompensa_id())
                    
                    if morador and recompensa:
                        with st.container():
                            col1, col2, col3 = st.columns([2, 1, 1])
                            
                            with col1:
                                st.write(f"**Morador:** {morador.get_nome()}")
                                st.write(f"**Recompensa:** {recompensa.get_nome()}")
                                st.write(f"**Data:** {DataUtil.formatar_data_hora(solicitacao.get_data())}")
                            
                            with col2:
                                st.write(f"{recompensa.get_pontos()} pontos")
                            
                            with col3:
                                col_a, col_r = st.columns(2)
                                with col_a:
                                    if st.button("Aprovar", key=f"aprovar_{solicitacao.get_id()}"):
                                        solicitacao.set_status("aprovada")
                                        SolicitacaoRecompensaDAO.atualizar(solicitacao)
                                        st.success("Solicitacao aprovada!")
                                        st.rerun()
                                
                                with col_r:
                                    if st.button("Rejeitar", key=f"rejeitar_{solicitacao.get_id()}"):
                                        morador.set_pontos(morador.get_pontos() + recompensa.get_pontos())
                                        MoradorDAO.atualizar(morador)  
                                        SolicitacaoRecompensaDAO.deletar(solicitacao.get_id())
                                        st.success("Solicitacao rejeitada! Pontos devolvidos ao morador.")
                                        st.rerun()
                            
                            st.divider()
            else:
                st.info("Nenhuma solicitação pendente.")
            st.write(f"**Solicitacoes Aprovadas ({len(aprovadas)}):**")
            if aprovadas:
                for solicitacao in aprovadas:
                    morador = MoradorDAO.buscar_por_id(solicitacao.get_morador_id())
                    recompensa = RecompensaDAO.buscar_por_id(solicitacao.get_recompensa_id())
                    
                    if morador and recompensa:
                        st.write(f"{morador.get_nome()} - {recompensa.get_nome()}")
        else:
            st.info("Nenhuma solicitação de recompensa.")
    
    @staticmethod
    def gerenciar_cooperativas():
        st.header("Gerenciar Cooperativas")
        
        tab1, tab2, tab3 = st.tabs(["Ver Todas", "Criar Nova", "Editar/Deletar"])
        
        # TAB 1: VER TODAS AS COOPERATIVAS
        with tab1:
            cooperativas = CooperativaDAO.listar()
            
            if cooperativas:
                st.subheader(f"Total de Cooperativas: {len(cooperativas)}")
                dados = []
                for c in cooperativas:
                    dados.append({
                        "ID": c.get_id(),
                        "Razão Social": c.get_razao(),
                        "CNPJ": c.get_cnpj(),
                        "Email": c.get_email(),
                        "Telefone": c.get_fone(),
                        "Endereço": c.get_endereco()
                    })
                
                st.dataframe(dados, use_container_width=True)
            else:
                st.info("Nenhuma cooperativa cadastrada.")
        
        # TAB 2: CRIAR NOVA COOPERATIVA
        with tab2:
            st.subheader("Cadastrar Nova Cooperativa")
            
            with st.form("form_nova_cooperativa"):
                razao_social = st.text_input("Razão Social*", placeholder="Nome da cooperativa")
                cnpj = st.text_input("CNPJ*", placeholder="00.000.000/0000-00")
                email = st.text_input("Email*", placeholder="exemplo@cooperativa.com")
                fone = st.text_input("Telefone*", placeholder="(00) 00000-0000")
                endereco = st.text_area("Endereço*", placeholder="Rua, Número, Bairro, Cidade, Estado")
                senha = st.text_input("Senha*", type="password", placeholder="Digite uma senha segura")
                confirmar_senha = st.text_input("Confirmar Senha*", type="password", placeholder="Confirme a senha")
                
                if st.form_submit_button("Cadastrar Cooperativa", use_container_width=True):
                    if not razao_social or not cnpj or not email or not fone or not endereco or not senha:
                        st.error("Preencha todos os campos obrigatórios!")
                    elif senha != confirmar_senha:
                        st.error("As senhas não coincidem!")
                    else:
                        from models.cooperativa import cooperativa
                        nova_cooperativa = cooperativa(
                            razaoSocial=razao_social,
                            cnpj=cnpj,
                            email=email,
                            fone=fone,
                            endereco=endereco,
                            senha=senha
                        )
                        
                        try:
                            CooperativaDAO.inserir(nova_cooperativa)
                            st.success("✅ Cooperativa cadastrada com sucesso!")
                            st.rerun()
                        except Exception as e:
                            st.error(f"❌ Erro ao cadastrar cooperativa: {str(e)}")
        
        # TAB 3: EDITAR OU DELETAR COOPERATIVA
        with tab3:
            cooperativas = CooperativaDAO.listar()
            
            if cooperativas:
                st.subheader("Selecione uma Cooperativa")
                
                opcoes = [f"{c.get_id()} - {c.get_razao()}" for c in cooperativas]
                cooperativa_selecionada = st.selectbox("Cooperativa:", opcoes, key="selecao_coop")
                
                cooperativa_id = int(cooperativa_selecionada.split(" - ")[0])
                cooperativa = CooperativaDAO.buscar_por_id(cooperativa_id)
                
                if cooperativa:
                    st.divider()
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.subheader("📝 Editar Dados")
                        with st.form(f"form_editar_cooperativa_{cooperativa_id}"):
                            razao_social = st.text_input("Razão Social", value=cooperativa.get_razao())
                            cnpj = st.text_input("CNPJ", value=str(cooperativa.get_cnpj()))
                            email = st.text_input("Email", value=cooperativa.get_email())
                            fone = st.text_input("Telefone", value=str(cooperativa.get_fone()))
                            endereco = st.text_area("Endereço", value=cooperativa.get_endereco())
                            
                            if st.form_submit_button("💾 Salvar Alterações", use_container_width=True):
                                cooperativa.set_razao(razao_social)
                                cooperativa.set_cnpj(cnpj)
                                cooperativa.set_email(email)
                                cooperativa.set_fone(fone)
                                cooperativa.set_endereco(endereco)
                                
                                try:
                                    CooperativaDAO.atualizar(cooperativa)
                                    st.success("✅ Cooperativa atualizada com sucesso!")
                                    st.rerun()
                                except Exception as e:
                                    st.error(f"❌ Erro ao atualizar: {str(e)}")
                    
                    with col2:
                        st.subheader("📋 Informações Atuais")
                        st.write(f"**ID:** {cooperativa.get_id()}")
                        st.write(f"**Razão Social:** {cooperativa.get_razao()}")
                        st.write(f"**CNPJ:** {cooperativa.get_cnpj()}")
                        st.write(f"**Email:** {cooperativa.get_email()}")
                        st.write(f"**Telefone:** {cooperativa.get_fone()}")
                        st.write(f"**Endereço:** {cooperativa.get_endereco()}")
                        
                        st.divider()
                        
                        if st.button("🗑️ Deletar Cooperativa", use_container_width=True, type="secondary"):
                            if st.session_state.get(f"confirmar_delete_{cooperativa_id}", False):
                                CooperativaDAO.deletar(cooperativa_id)
                                st.success("✅ Cooperativa deletada com sucesso!")
                                st.rerun()
                            else:
                                st.warning(f"⚠️ Tem certeza que deseja deletar {cooperativa.get_razao()}?")
                                st.session_state[f"confirmar_delete_{cooperativa_id}"] = True
            else:
                st.info("Nenhuma cooperativa cadastrada.")