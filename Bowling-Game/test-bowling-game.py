"""Regras de pontuação do bowling

Um jogo tem 10 jogadas (frames). Em cada jogada há 10 pinos e, em geral, até dois lançamentos para os derrubar.

Jogada normal (open frame): não derrubaram os 10 pinos nos dois lançamentos. 
A pontuação da jogada é só a soma dos pinos. Exemplo: 3 + 4 = 7.

Spare: derrubaram os 10 pinos com os dois lançamentos (ex.: 6 + 4). 
A jogada vale 10 + os pinos do lançamento seguinte. Exemplo: spare seguido de um 5 vale 10 + 5 = 15.

Strike: derrubaram os 10 pinos no primeiro lançamento. 
A jogada acaba logo e vale 10 + os pinos dos dois lançamentos seguintes. 
Exemplo: strike seguido de 3 e 4 vale 10 + 3 + 4 = 17.

Décima jogada: se fizerem spare ou strike na última jogada, 
ganham lançamentos extra para calcular o bónus: 1 extra para um spare, 2 extra para um strike. 
Esses lançamentos só servem de bónus, não contam como jogada nova. 
Por isso, a décima jogada pode ter até 3 lançamentos."""

