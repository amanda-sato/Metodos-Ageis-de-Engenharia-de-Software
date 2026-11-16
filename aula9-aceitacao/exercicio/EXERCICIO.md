# Exercício — levantar equipamento reservado

## A história

Como técnico do laboratório, quero registar o levantamento de um equipamento
reservado, para saber quem o tem.

## O que a cliente disse

> «Só se levanta o que se reservou, e dentro das datas da reserva: do primeiro
> ao último dia, os dois incluídos. Antes disso, não. Depois disso, a reserva
> expirou. Quem tem equipamento em atraso não leva mais nada enquanto não o
> devolver. Atenção: em atraso é quando o dia da devolução prevista já passou;
> quem tem de devolver hoje ainda está dentro do prazo. E se o equipamento
> estiver em manutenção, não sai, com ou sem reserva.»

## O que têm de fazer

1. **Tabela de exemplos.** Antes de abrir o código, criem `exemplos.md` com
   uma tabela. Usem sempre a mesma reserva: câmara, de 10 a 12 de novembro.

   | # | Dado (contexto) | Quando (dia do levantamento) | Então | Regra |
   | - | --------------- | ---------------------------- | ----- | ----- |
   | 1 | sem empréstimos | 11 nov | aceite | dentro das datas |
   | 2 | ... | ... | ... | ... |

   Para cada regra da cliente, escrevam um exemplo de cada lado da fronteira.
   Devem chegar a 9 ou 10 exemplos.

2. **Testes de aceitação.** Passem cada linha da tabela para um teste em
   `tests/aceitacao/test_levantamento.py`, com o nome no formato
   `test_dado_..._quando_..._entao_...`. Façam um commit por exemplo.

3. **Corram os testes.**

       python3 -m pytest -v

4. **Verifiquem o resultado** (é assim que sabem se a tabela está boa):

   - Se **todos passam**, faltam exemplos na fronteira. Voltem ao passo 1 e
     releiam as palavras «incluídos» e «hoje» no que a cliente disse.
   - Se **exatamente dois falham**, encontraram os dois defeitos. Avancem.
   - Se **falham mais de dois**, um dos vossos exemplos contradiz a cliente.
     Releiam a citação e corrijam o exemplo, não o código.

5. **Corrijam o código.** Com os dois testes vermelhos, corrijam
   `levantamento.py` — um defeito de cada vez, um commit `green:` por cada.
   Cada correção é mínima: um único carácter.

6. **Respondam por escrito** em `RETRO.md` (três ou quatro linhas chegam):
   - Que exemplos encontraram os defeitos? O que têm em comum?
   - Um teste unitário escrito por quem fez o código teria encontrado estes
     defeitos? Porquê?
