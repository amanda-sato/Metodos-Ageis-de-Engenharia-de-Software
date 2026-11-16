"""Levantamento de equipamento reservado.

ATENÇÃO: este módulo foi escrito à pressa e tem DOIS defeitos.
Não os procurem a ler o código: escrevam os exemplos da cliente como
testes de aceitação e deixem que sejam os testes a encontrá-los.
"""
from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Reserva:
    item: str
    inicio: date
    fim: date
    utilizador: str


@dataclass(frozen=True)
class Emprestimo:
    """Um equipamento que o utilizador tem consigo."""
    item: str
    devolucao_prevista: date


@dataclass(frozen=True)
class Resultado:
    aceite: bool
    motivo: str = ""


def levantar(reserva, hoje, emprestimos=(), em_manutencao=False):
    """Decide se o utilizador pode levantar hoje o item que reservou.

    emprestimos: os equipamentos que o utilizador tem consigo neste momento.
    """
    if em_manutencao:
        return Resultado(False, "equipamento em manutenção")
    if any(e.devolucao_prevista <= hoje for e in emprestimos):
        return Resultado(False, "tem equipamento em atraso")
    if hoje < reserva.inicio:
        return Resultado(False, "a reserva ainda não começou")
    if hoje >= reserva.fim:
        return Resultado(False, "a reserva expirou")
    return Resultado(True)
