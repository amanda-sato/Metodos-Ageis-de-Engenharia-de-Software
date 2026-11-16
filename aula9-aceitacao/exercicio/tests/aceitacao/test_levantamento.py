"""Testes de aceitação da história «levantar equipamento reservado».

O primeiro exemplo está feito. Acrescentem os restantes a partir da vossa
tabela de exemplos (ver EXERCICIO.md).
"""
from datetime import date

from levantamento import Emprestimo, Reserva, levantar

# Dado: a Ana reservou a câmara de 10 a 12 de novembro.
RESERVA = Reserva("camara", date(2026, 11, 10), date(2026, 11, 12), "ana")


def test_dado_reserva_10_a_12_quando_levanta_a_11_entao_aceita():
    resultado = levantar(RESERVA, hoje=date(2026, 11, 11))
    assert resultado.aceite


# Exemplo de como usar empréstimos e motivo (apaguem ou adaptem):
#
# def test_dado_..._quando_..._entao_...():
#     emprestimos = [Emprestimo("tripe", devolucao_prevista=date(2026, 11, 20))]
#     resultado = levantar(RESERVA, hoje=date(2026, 11, 11), emprestimos=emprestimos)
#     assert not resultado.aceite
#     assert resultado.motivo == "..."
