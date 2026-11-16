"""Testes unitários: uma função, sem dependências. Dizem ao programador se a peça funciona."""
from datetime import date

from reservas.servico import sobrepoem


def test_periodos_separados_nao_se_sobrepoem():
    assert not sobrepoem(date(2026, 10, 5), date(2026, 10, 8),
                         date(2026, 10, 9), date(2026, 10, 12))


def test_periodos_que_partilham_um_dia_sobrepoem_se():
    assert sobrepoem(date(2026, 10, 5), date(2026, 10, 8),
                     date(2026, 10, 8), date(2026, 10, 10))


def test_periodo_contido_noutro_sobrepoe_se():
    assert sobrepoem(date(2026, 10, 5), date(2026, 10, 8),
                     date(2026, 10, 6), date(2026, 10, 7))
