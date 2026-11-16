"""Testes de aceitação da história «impedir reservas em conflito».

História: Como técnico, quero impedir reservas em conflito,
para não prometer o mesmo equipamento duas vezes.

Cada teste é um exemplo combinado com a cliente. Usam o vocabulário da
cliente (câmara, reservar, recusar) e entram pelo serviço, não pelas
funções internas.
"""
from datetime import date

import pytest

from reservas.repositorio import RepositorioMemoria
from reservas.servico import ReservaRecusada, ServicoReservas


@pytest.fixture
def servico():
    """Dado: uma câmara já reservada de 5 a 8 de outubro."""
    servico = ServicoReservas(RepositorioMemoria())
    servico.reservar("camara", date(2026, 10, 5), date(2026, 10, 8), "ana")
    return servico


def test_dado_camara_reservada_5_a_8_quando_reservo_7_a_10_entao_recusa_e_indica_dia_9(servico):
    # Quando
    with pytest.raises(ReservaRecusada) as recusa:
        servico.reservar("camara", date(2026, 10, 7), date(2026, 10, 10), "rui")
    # Então
    assert recusa.value.data_livre == date(2026, 10, 9)


def test_dado_camara_reservada_5_a_8_quando_reservo_a_partir_de_9_entao_aceita(servico):
    # Quando
    reserva = servico.reservar("camara", date(2026, 10, 9), date(2026, 10, 12), "rui")
    # Então
    assert reserva.utilizador == "rui"


def test_dado_camara_reservada_quando_reservo_outro_item_nas_mesmas_datas_entao_aceita(servico):
    reserva = servico.reservar("tripe", date(2026, 10, 5), date(2026, 10, 8), "rui")
    assert reserva.item == "tripe"


# A mesma regra como tabela de exemplos: cada linha é um exemplo-chave.
# Câmara reservada de 5 a 8 de outubro.
@pytest.mark.parametrize(
    "dia_inicio, dia_fim, aceite",
    [
        (1, 4, True),    # termina na véspera: fronteira, aceite
        (1, 5, False),   # termina no primeiro dia ocupado: fronteira, recusada
        (6, 7, False),   # dentro do período ocupado
        (8, 10, False),  # começa no último dia ocupado: fronteira, recusada
        (9, 10, True),   # começa no dia seguinte: fronteira, aceite
    ],
)
def test_tabela_de_exemplos_de_conflito(servico, dia_inicio, dia_fim, aceite):
    inicio, fim = date(2026, 10, dia_inicio), date(2026, 10, dia_fim)
    if aceite:
        assert servico.reservar("camara", inicio, fim, "rui")
    else:
        with pytest.raises(ReservaRecusada):
            servico.reservar("camara", inicio, fim, "rui")
