# Retrospetiva da iteração 2

## A ação da retrospetiva 1 foi aplicada? Como?
- Sim. A ação era confirmar os termos do glossário antes de cada história e testar cada estado possível.
  - Antes da H06, confirmei no glossário que um empréstimo só começa no levantamento e termina na devolução. Por isso criei o `levantar` e o `devolver`, em vez de tratar qualquer reserva como empréstimo.
  - O mesmo glossário mostrou um erro que nenhum critério apanhava: empréstimos já devolvidos ainda apareciam na consulta. Escrevi um teste para isso e corrigi.
  - Os termos "atraso" e "bloqueio" do glossário deram nome aos métodos `em_atraso` e `verificar_bloqueio`.
  - Cada situação de um empréstimo tem o seu teste: faltam N dias, falta 1 dia, termina hoje, em atraso e devolvido.

## O que manter
- TDD em passos pequenos: um teste vermelho de cada vez, o mínimo para ficar verde e só depois refatorizar.
- Um teste de aceitação por critério, com o nome no formato Dado / Quando / Então. Tornou fácil ver o que estava coberto.
- Refatorizar logo que aparece repetição. Mover a lógica para a `Reserva` (`situacao_em`, `em_emprestimo`, `em_atraso`) fez com que a H09 saísse quase sem código novo.
- Quando um teste passa à primeira, estragar o código de propósito para confirmar que o teste consegue falhar.

## O que mudar
- O plano do sprint e o diário começaram tarde, quando o sprint já ia avançado. O diário perde valor como evidência se não for escrito dia a dia.
- Perdi tempo com o ambiente: duas versões do Python instaladas, o pytest só numa delas, e a mudança do nome da pasta. Devia ter confirmado o ambiente antes de começar a programar.
- As questões em aberto (Q1 a Q7) continuam sem resposta da cliente. Fiz o código à volta delas, mas devia tê-las enviado mais cedo.

## Uma ação concreta para a iteração 3 (Kanban)
- No primeiro dia da iteração 3, enviar à cliente todas as questões em aberto (Q1 a Q7) e só puxar a H10 para "em curso" depois de a Q3 (durante quanto tempo se guarda o histórico) estar respondida.