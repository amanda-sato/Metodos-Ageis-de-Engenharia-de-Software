# Retrospetiva da iteração 1

## O que correu bem
- Os testes foram escritos a partir das regras do enunciado (reservas sobrepostas, devolução em feriado, regra das 48 horas para docentes, formação de kits), o que ajudou a detetar erros cedo.
- As funções principais (`reservar`, `docente_pode_passar_a_frente`, `estado_em`) ficaram simples e com responsabilidades bem separadas.
- O uso do Claude IA acelerou a escrita de testes e ajudou a lembrar casos-limite, desde que as sugestões fossem revistas antes de aceitar.


## O que correu mal ou mudaria

- No H04, o estado_em não olhava para a manutenção. Um item em manutenção sem reservas aparece como “disponível” nesta consulta, e o glossário diz que deve ser “indisponível”, então acrescentei isso no H04.

## Uma ação concreta para a iteração 2
- Antes de implementar cada história, confirmar os termos usados no glossário (ex.: "disponível", "indisponível", "em espera") e escrever pelo menos um teste para cada estado possível do item, incluindo a manutenção.



Questões para o cliente:

H07 - 
Q2: um estudante pode ceder a reserva a outro?
Q5: quando um docente fica com o item, o estudante deve ser avisado?