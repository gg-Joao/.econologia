## CASO DE USO: Abrir Conta
CASO DE USO: Abrir Conta
Atores envolvidos: Usuário (Morador ou Cooperativa)
Pré-condições: O usuário não possui cadastro no sistema.
Pós-condições: A conta do usuário é criada e armazenada no sistema.
Fluxo principal:
 1. O usuário seleciona a opção Abrir Conta de Morador ou Abrir Conta de
 Cooperativa.
 2. O usuário informa os dados solicitados.
   ○ Morador: nome, e-mail, telefone e senha.
   ○ Cooperativa: razão social, CNPJ, e-mail, endereço, telefone e senha.
 3. O sistema valida as informações.
 4. O sistema registra o usuário no banco de dados.
 5. O sistema informa que a conta foi criada com sucesso.
Fluxo de exceção: Dado incompleto ou inválido
O sistema rejeita o cadastro e solicita a correção dos dados. O caso de uso retorna
ao passo 2.
Modelo de interação associado: Diagrama de sequência
