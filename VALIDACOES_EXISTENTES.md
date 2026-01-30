# Lista de Validações do Sistema - Econologia

## 📋 Validações de Cadastro

### 1. **Cadastro de Morador**
   - ✅ Validação de campos vazios
   - ✅ Validação de formato e comprimento de NOME (3-50 caracteres, apenas letras e espaços)
   - ✅ Validação de formato de EMAIL (5-100 caracteres, padrão: usuario@dominio.com)
   - ✅ Validação de TELEFONE (10-11 dígitos, formato brasileiro)
   - ✅ Validação de comprimento de SENHA (6-20 caracteres)
   - ✅ Confirmação de senha (senha = confirmar_senha)
   - **Campos obrigatórios**: Nome, Email, Telefone, Senha
   - **Arquivo**: [templates/morador/cadastro_moradorUI.py](templates/morador/cadastro_moradorUI.py)
   - **Status**: ✅ Totalmente validado

### 2. **Cadastro de Cooperativa**
   - ✅ Validação de campos vazios
   - ✅ Validação de formato e comprimento de RAZÃO SOCIAL (3-100 caracteres)
   - ✅ Validação de CNPJ (exatamente 14 dígitos, formato: XX.XXX.XXX/XXXX-XX)
   - ✅ Validação de formato de EMAIL (5-100 caracteres, padrão: usuario@dominio.com)
   - ✅ Validação de ENDEREÇO (5-200 caracteres)
   - ✅ Validação de TELEFONE (10-11 dígitos, formato brasileiro)
   - ✅ Validação de comprimento de SENHA (6-20 caracteres)
   - ✅ Confirmação de senha (senha = confirmar_senha)
   - **Campos obrigatórios**: Razão Social, CNPJ, Email, Endereço, Telefone, Senha
   - **Arquivo**: [templates/cooperativa/cadastro_cooperativaUI.py](templates/cooperativa/cadastro_cooperativaUI.py)
   - **Status**: ✅ Totalmente validado

---

## 🔐 Validações de Login

### 3. **Login de Morador**
   - ✅ Validação de credenciais (email e senha)
   - Verifica se email e senha correspondem aos dados no banco
   - **Arquivo**: [templates/morador/login_moradorUI.py](templates/morador/login_moradorUI.py)

### 4. **Login de Cooperativa**
   - ✅ Validação de credenciais (email e senha)
   - Verifica se email e senha correspondem aos dados no banco
   - **Arquivo**: [templates/cooperativa/login_cooperativaUI.py](templates/cooperativa/login_cooperativaUI.py)

### 5. **Login de Administrador**
   - ✅ Validação de credenciais (email e senha)
   - Verifica se email e senha correspondem aos dados no banco
   - **Arquivo**: [templates/admin/login_adminUI.py](templates/admin/login_adminUI.py)

---

## 📅 Validações de Agendamento de Coleta

### 6. **Agendar Coleta**
   - ✅ Validação de descrição não vazia
   - ✅ Validação de data (não pode ser no passado)
   - **Regras**:
     - Campo de descrição deve estar preenchido (`.strip()`)
     - Data selecionada não pode ser menor que a data atual
   - **Arquivo**: [templates/morador/agendarColetaUI.py](templates/morador/agendarColetaUI.py#L28)
   - **Mensagens de erro**:
     - "Descreva os materiais."
     - "A data não pode ser no passado."

---

## 📍 Validações de Pontos de Coleta

### 7. **Adicionar Ponto de Coleta**
   - ✅ Validação de campos obrigatórios
   - ✅ Validação de horário (horário fim > horário início)
   - **Campos obrigatórios**: Nome, Endereço, Telefone, Horário Início, Horário Fim
   - **Arquivo**: [templates/admin/painel_adminUI.py](templates/admin/painel_adminUI.py#L240)
   - **Mensagens de erro**:
     - "Preencha todos os campos!"
     - "O horário de fim deve ser maior que o horário de início!"

### 8. **Editar Ponto de Coleta**
   - ✅ Validação de horário (horário fim > horário início)
   - **Arquivo**: [templates/admin/painel_adminUI.py](templates/admin/painel_adminUI.py#L305)

---

## 🎁 Validações de Recompensas

### 9. **Adicionar Recompensa**
   - ✅ Validação de campos obrigatórios (nome e descrição)
   - **Campos obrigatórios**: Nome, Descrição
   - **Campo com validação de valor mínimo**: Pontos (mínimo 1)
   - **Arquivo**: [templates/admin/painel_adminUI.py](templates/admin/painel_adminUI.py#L350)
   - **Mensagem de erro**: "Preencha todos os campos."

### 10. **Resgatar Recompensa**
   - ✅ Validação de saldo de pontos suficientes
   - Compara pontos atuais com pontos necessários
   - **Arquivo**: [templates/morador/recompensasUI.py](templates/morador/recompensasUI.py#L43)
   - **Lógica**: Apenas permite resgate se `pontos_atuais >= pontos_necessarios`

---

## 🗄️ Validações de Banco de Dados

### 11. **Constraints de Banco de Dados**
   - ✅ **CNPJ de Cooperativa**: UNIQUE (não permite CNPJs duplicados)
   - ✅ **Email de Cooperativa**: UNIQUE (não permite emails duplicados)
   - ✅ **Chaves Estrangeiras**: 
     - `solicitacao_recompensa.morador_id` referencia `morador.id`
     - `solicitacao_recompensa.recompensa_id` referencia `recompensa.id`
   - **Arquivo**: [POO/programa/database.py](database.py#L56)

---

## 📊 Resumo das Validações por Categoria

| Categoria | Total | ✅ Implementadas | ❌ Ausentes |
|-----------|-------|------------------|-----------|
| **Cadastro** | 2 | 2 | 0 |
| **Login** | 3 | 3 | 0 |
| **Agendamento** | 1 | 1 | 0 |
| **Pontos de Coleta** | 2 | 2 | 0 |
| **Recompensas** | 2 | 2 | 0 |
| **Banco de Dados** | 1 | 1 | 0 |
| **TOTAL** | **11** | **11** | **0** |

---

## 🚀 Recomendações para Melhorias

### Validações Implementadas com Sucesso ✅
Todos os campos de cadastro agora possuem:
- **Padrões de formato** (regex) para cada tipo de dado
- **Limites de caracteres** (mínimo e máximo)
- **Mensagens de erro claras** indicando o problema
- **Formatação visual** dos limites na interface

### Padrões de Validação Implementados:

| Campo | Mínimo | Máximo | Padrão |
|-------|--------|--------|---------|
| **Nome** | 3 | 50 | Apenas letras e espaços |
| **Email** | 5 | 100 | usuario@dominio.com |
| **Telefone** | 10 dígitos | 11 dígitos | Formato brasileiro |
| **Senha** | 6 | 20 | Caracteres variados |
| **CNPJ** | 14 | 14 | Exatamente 14 dígitos |
| **Razão Social** | 3 | 100 | Letras, números, espaços |
| **Endereço** | 5 | 200 | Caracteres variados |

### Utilitário de Validação:
- Arquivo: [utils/validacao_util.py](utils/validacao_util.py)
- Funções disponíveis para reutilização em outras partes do sistema
- Métodos de formatação para apresentação (ex: CNPJ, Telefone)

---

## 📝 Notas Técnicas

- **Framework**: Streamlit
- **Banco de Dados**: SQLite
- **Padrão DAO**: Implementado com BaseDAO
- **Modelos**: Classes com getters e setters
- **Utilitários**: Classe `DataUtil` para formatação de datas

