# Backlog do produto

> Modelo para o Projeto Prático (M1). Substituam o texto entre parênteses retos e apaguem
> estas linhas de instruções antes da primeira entrega. Este ficheiro vive no repositório e é
> atualizado em cada iteração — é o contrato com a cliente.

**Produto:** ReservaLab — Gestão de Equipamento do Laboratório Multimédia
**Equipa:** Amanda Reiko de Oliveira Sato
**Cliente:** Célia Soares
**Última atualização:** 10 out 2026

---

## Visão

Para a responsável do laboratório multimédia, os técnicos, os estudantes e os docentes que
requisitam equipamento, o ReservaLab substitui a folha de cálculo e o caderno: mostra o que
existe, onde está e quando está livre, e impede que o mesmo equipamento seja prometido a duas
pessoas. Com ele, a responsável é avisada a tempo do material por devolver e consegue responder
à direção sobre o equipamento mais usado.

## Definição de pronto

Acordada na aula 3. Uma história só está pronta quando:

- [ ] todos os critérios de aceitação estão cobertos por testes automáticos;
- [ ] todos os testes passam na integração contínua;
- [ ] o código foi refatorizado e não deixou duplicação óbvia;
- [ ] está integrado no ramo principal, sem trabalho por juntar;
- [ ] este ficheiro está atualizado;
- [ ] a cliente viu a funcionar e aceitou.

## Glossário

| Termo | Significado |
|---|---|
| Item | Uma peça de equipamento individual, com identificação própria. |
| Kit | Conjunto de itens emprestados e devolvidos em conjunto. |
| Reserva | Intenção de levantar um item ou kit num intervalo de datas. |
| Empréstimo | Período entre o levantamento e a devolução de um item ou kit. |
| Levantamento | Momento em que o equipamento sai do laboratório. |
| Devolução | Momento em que o equipamento regressa e é verificado. |
| Atraso | Situação em que a devolução não aconteceu até à data prevista. |
| Bloqueio | Impedimento de fazer novas reservas enquanto houver material em atraso. |
| Manutenção | Estado em que um item não pode ser reservado nem levantado. |
| Disponível | Estado de um item, num intervalo de datas, sem nenhuma reserva. |
| Em espera | Estado de um item reservado por um estudante, que ainda pode ser reservado por um docente até 48 horas antes do início da reserva. |
| Indisponível | Estado de um item que já não pode ser reservado nesse intervalo de datas, ou que está em manutenção. |
| Localização | Sítio onde o item se encontra: no laboratório (com o local de arrumação) ou com quem o levantou. |

## Estado das iterações

| Iteração | Período | Pontos planeados | Pontos concluídos | Notas |
|---|---|---|---|---|
| 1 | 12 out – 2 nov | 26 | | H01, H02, H03, H04, H05, H07 — saber o que existe e reservar sem conflitos |
| 2 | 2 nov – 16 nov | 8 | | H06, H08, H09 — prazos, alertas e bloqueios |
| 3 | 16 nov – 11 jan | 5 | | H10 — estatísticas de uso |

---

## Histórias

Cada história tem identificador, estimativa em pontos, prioridade atribuída pela cliente e
estado. Os critérios de aceitação são escritos em Dado / Quando / Então e dão origem aos testes.

Prioridade: **1** = a cliente quer já · **2** = quer nesta iteração se couber · **3** = pode esperar.
Estado: `por fazer` · `em curso` · `pronto` · `aceite`

### H01 — Ver o equipamento existente

**Como** estudante, **quero** ver a lista do equipamento do laboratório, **para** saber o que
posso requisitar.

- **Pontos:** 2 · **Prioridade:** 1 · **Iteração:** 1 · **Estado:** por fazer

**Critérios de aceitação**

1. Dado que existem itens registados, quando consulto a lista, então vejo o nome e o tipo de cada item.
2. Dado que um item está em manutenção, quando consulto a lista, então esse item aparece assinalado como indisponível.
3. Dado que não existe nenhum item registado, quando consulto a lista, então recebo uma mensagem a dizer que não há equipamento.

---

### H02 — Reservar um item num intervalo de datas

**Como** estudante, **quero** reservar um item entre duas datas, **para** garantir que está
disponível quando preciso dele.

- **Pontos:** 3 · **Prioridade:** 1 · **Iteração:** 1 · **Estado:** por fazer

**Critérios de aceitação**

1. Dado um item disponível, quando o reservo de 5 a 8 de outubro, então a reserva fica registada com essas datas.
2. Dado um item disponível, quando tento reservá-lo por mais de sete dias corridos, então a reserva é recusada com a indicação do limite.
3. Dado um item em manutenção, quando tento reservá-lo, então a reserva é recusada.

---

### H03 — Recusar reservas em conflito

**Como** técnico do laboratório, **quero** que o sistema recuse reservas sobrepostas, **para**
não prometer o mesmo equipamento a duas pessoas.

- **Pontos:** 5 · **Prioridade:** 1 · **Iteração:** 1 · **Estado:** por fazer

**Critérios de aceitação**

1. Dada uma câmara reservada de 5 a 8 de outubro, quando alguém tenta reservá-la de 7 a 10 de outubro, então a reserva é recusada e é indicada a data livre seguinte.
2. Dada uma câmara reservada de 5 a 8 de outubro, quando alguém a reserva a partir de 9 de outubro, então a reserva é aceite.
3. Dado um kit reservado, quando alguém tenta reservar um dos seus itens em separado nas mesmas datas, então a reserva é recusada.

---

### H04 — Ver estado, localização e kits possíveis

**Como** responsável pelo laboratório multimédia, **quero** visualizar que equipamentos estão
"disponíveis" e "em espera", a sua localização e se tenho quantidade suficiente para formar um
kit, **para** saber o que posso emprestar sem folhear o caderno.

- **Pontos:** 5 · **Prioridade:** 1 · **Iteração:** 1 · **Estado:** por fazer

**Critérios de aceitação**

1. Dado que existem itens disponíveis e em espera numa data, quando consulto o equipamento para essa data, então vejo o estado de cada item.
2. Dado um item, quando consulto os seus detalhes, então vejo a sua localização.
3. Dado que existem duas câmaras, dois tripés e dois microfones disponíveis numa data, quando consulto os kits possíveis, então o sistema indica que é possível formar dois kits.
4. Dado que não há nenhum microfone disponível numa data, quando consulto os kits possíveis, então o sistema indica que não é possível formar nenhum kit.

---

### H05 — Limitar o empréstimo a sete dias corridos

**Como** responsável pelo laboratório multimédia, **quero** que o prazo máximo de empréstimo
seja de sete dias corridos e que, se terminar num feriado, passe para o dia útil seguinte,
**para** evitar empréstimos muito longos que atrapalhem outros utilizadores.

- **Pontos:** 3 · **Prioridade:** 1 · **Iteração:** 1 · **Estado:** por fazer

**Critérios de aceitação**

1. Dado um item disponível, quando alguém o reserva de 10 a 17 de novembro, então a reserva é aceite com devolução a 17 de novembro.
2. Dado um item disponível, quando alguém tenta reservá-lo de 10 a 18 de novembro, então a reserva é recusada com a indicação do limite.
3. Dado que 1 de dezembro é feriado, quando alguém reserva um item de 24 de novembro a 1 de dezembro, então a devolução passa para 2 de dezembro.

---

### H06 — Ver o tempo restante de cada empréstimo

**Como** responsável pelo laboratório multimédia, **quero** saber quanto tempo falta até ao fim
do empréstimo de cada item, **para** planear os próximos empréstimos e antecipar atrasos.

- **Pontos:** 2 · **Prioridade:** 2 · **Iteração:** 2 · **Estado:** por fazer

**Critérios de aceitação**

1. Dado um item com devolução a 20 de novembro, quando consulto os empréstimos a 17 de novembro, então vejo que faltam 3 dias.
2. Dado um item cuja devolução é hoje, quando consulto os empréstimos, então vejo que termina hoje.
3. Dado um item cujo prazo já passou, quando consulto os empréstimos, então esse item aparece assinalado como em atraso.

---

### H07 — Dar prioridade aos docentes até 48 horas antes

**Como** responsável pelo laboratório multimédia, **quero** que os estudantes só reservem itens
"disponíveis", que um item reservado por um estudante fique "em espera" e só possa ser
reservado por um docente até 48 horas antes da data da reserva, passando depois a
"indisponível", e que os docentes possam reservar itens "disponíveis" e "em espera", **para**
que não haja conflitos de empréstimo de equipamento.

- **Pontos:** 8 · **Prioridade:** 1 · **Iteração:** 1 · **Estado:** por fazer

**Critérios de aceitação**

1. Dado um item disponível, quando um estudante o reserva, então a reserva é aceite e o item fica em espera nessas datas.
2. Dado um item em espera, quando outro estudante tenta reservá-lo nas mesmas datas, então a reserva é recusada.
3. Dado um item em espera com reserva a começar a 20 de novembro, quando um docente o reserva a 17 de novembro, então a reserva do docente é aceite, o item fica indisponível e a reserva do estudante é cancelada.
4. Dado um item em espera com reserva a começar a 20 de novembro, quando um docente tenta reservá-lo a 19 de novembro, então a reserva é recusada.
5. Dado um item em espera, quando faltam 48 horas para o início da reserva, então o item passa a indisponível.
6. Dado um item disponível, quando um docente o reserva, então a reserva é aceite e o item fica indisponível nessas datas.

---

### H08 — Alertar sobre o fim do prazo

**Como** responsável pelo laboratório multimédia, **quero** ser alertada um dia antes e no dia
do fim do prazo de um empréstimo, **para** ter conhecimento dos prazos.

- **Pontos:** 3 · **Prioridade:** 2 · **Iteração:** 2 · **Estado:** por fazer

**Critérios de aceitação**

1. Dado um empréstimo com devolução a 20 de novembro, quando chega o dia 19 de novembro, então recebo um alerta de que o prazo termina amanhã.
2. Dado um empréstimo com devolução a 20 de novembro, quando chega o dia 20 de novembro, então recebo um alerta de que o prazo termina hoje.
3. Dado um item devolvido antes do prazo, quando chega o dia do fim do prazo, então não recebo alerta.

---

### H09 — Bloquear quem passou do prazo

**Como** responsável pelo laboratório multimédia, **quero** que os perfis de quem passou do
prazo fiquem bloqueados, **para** evitar que façam novos empréstimos sem terem devolvido os
itens anteriores.

- **Pontos:** 3 · **Prioridade:** 2 · **Iteração:** 2 · **Estado:** por fazer

**Critérios de aceitação**

1. Dado um utilizador com um item cujo prazo terminou e que não o devolveu, quando tenta fazer uma reserva, então a reserva é recusada com a indicação do item em atraso.
2. Dado um utilizador bloqueado, quando o técnico regista a devolução do item em atraso, então o utilizador volta a poder fazer reservas.
3. Dado um utilizador com dois itens em atraso, quando devolve só um, então continua bloqueado.

---

### H10 — Contar empréstimos e mostrar um gráfico de uso

**Como** responsável pelo laboratório multimédia, **quero** que o sistema mantenha atualizado o
número de vezes que cada item é emprestado e gere um gráfico, **para** saber quais os itens
mais e menos utilizados.

- **Pontos:** 5 · **Prioridade:** 3 · **Iteração:** 3 · **Estado:** por fazer

**Critérios de aceitação**

1. Dado um item emprestado 3 vezes, quando é levantado mais uma vez, então a sua contagem passa para 4.
2. Dado uma reserva cancelada antes do levantamento, quando consulto a contagem, então essa reserva não é contada.
3. Dado que existem itens com contagens diferentes, quando abro o gráfico, então vejo os itens ordenados do mais para o menos emprestado.
4. Dado um item que nunca foi emprestado, quando abro o gráfico, então esse item aparece com zero empréstimos.

---

## Questões em aberto

Perguntas que precisam de resposta da cliente antes de a história poder ser estimada ou feita.

| # | Questão | Bloqueia | Estado |
|---|---|---|---|
| Q1 | O que fazer quando o equipamento é devolvido com danos? | H09 | à espera de resposta |
| Q2 | Um estudante pode ceder a reserva a outro? | H07 | à espera de resposta |
| Q3 | Durante quanto tempo se guarda o histórico? | H10 | à espera de resposta |
| Q4 | Que feriados contam (nacionais, municipais, encerramentos da universidade)? Os fins de semana também adiam o prazo? | H05 | à espera de resposta |
| Q5 | Quando um docente fica com um item em espera, o estudante deve ser avisado? | H07 | à espera de resposta |
| Q6 | Como chegam os alertas (no sistema, por email)? Quem os recebe além da responsável? | H08 | à espera de resposta |
| Q7 | Que detalhe é preciso na localização (laboratório, armário, prateleira)? | H04 | à espera de resposta |

## Fora do âmbito

Registado para não voltar à discussão a cada iteração:

- pagamentos e cauções;
- leitura de códigos de barras;
- aplicação para telemóvel;
- ligação aos sistemas da universidade;
- reservas repetidas automaticamente.
