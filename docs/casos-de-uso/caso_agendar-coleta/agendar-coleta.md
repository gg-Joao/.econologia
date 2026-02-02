 ## CASO DE USO: Agendar Coleta

Atores envolvidos: Usuário (Morador)
Pré-condições: O morador está cadastrado, autenticado e existem cooperativas
disponíveis.
Pós-condições: A coleta é registrada no sistema.

Fluxo principal:
 1. O morador acessa a funcionalidade Agendar Coleta.

 2. O morador seleciona o tipo de resíduo.

 3. O sistema apresenta as cooperativas disponíveis.

 4. O morador escolhe a cooperativa.

 5. O morador seleciona a data da coleta.

 6. O sistema verifica a disponibilidade.

 7. O sistema registra o agendamento.
 
 8. O sistema confirma o agendamento.

Fluxo alternativo: Data indisponível
O sistema informa a indisponibilidade e solicita nova data.

Fluxo de exceção: Falha na comunicação
O sistema informa erro e encerra o processo.
Modelo de interação associado: Diagrama de sequência.
