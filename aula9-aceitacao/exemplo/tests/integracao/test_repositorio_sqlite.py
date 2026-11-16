"""Testes de integração: o nosso código com uma base de dados verdadeira.

Não repetem as regras de negócio. Verificam o que os duplos de teste não
conseguem verificar: que o SQL está certo e que as datas sobrevivem à
ida e volta ao disco.
"""
from datetime import date

import pytest

from reservas.repositorio import RepositorioSQLite
from reservas.servico import Reserva, ReservaRecusada, ServicoReservas

pytestmark = pytest.mark.integracao


def test_reserva_guardada_volta_igual(tmp_path):
    repositorio = RepositorioSQLite(tmp_path / "reservas.db")
    reserva = Reserva("camara", date(2026, 10, 5), date(2026, 10, 8), "ana")

    repositorio.guardar(reserva)

    assert repositorio.reservas_do_item("camara") == [reserva]


def test_reservas_persistem_entre_ligacoes(tmp_path):
    caminho = tmp_path / "reservas.db"
    RepositorioSQLite(caminho).guardar(
        Reserva("camara", date(2026, 10, 5), date(2026, 10, 8), "ana"))

    outro = RepositorioSQLite(caminho)  # como se a aplicação reiniciasse

    assert len(outro.reservas_do_item("camara")) == 1


def test_so_devolve_reservas_do_item_pedido(tmp_path):
    repositorio = RepositorioSQLite(tmp_path / "reservas.db")
    repositorio.guardar(Reserva("camara", date(2026, 10, 5), date(2026, 10, 8), "ana"))
    repositorio.guardar(Reserva("tripe", date(2026, 10, 5), date(2026, 10, 8), "rui"))

    assert [r.item for r in repositorio.reservas_do_item("tripe")] == ["tripe"]


def test_servico_com_base_de_dados_real_recusa_conflito(tmp_path):
    servico = ServicoReservas(RepositorioSQLite(tmp_path / "reservas.db"))
    servico.reservar("camara", date(2026, 10, 5), date(2026, 10, 8), "ana")

    with pytest.raises(ReservaRecusada):
        servico.reservar("camara", date(2026, 10, 7), date(2026, 10, 10), "rui")
