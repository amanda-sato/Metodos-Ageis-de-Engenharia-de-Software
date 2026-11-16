"""Regras de negócio das reservas. Não sabe onde os dados são guardados."""
from dataclasses import dataclass
from datetime import date, timedelta


@dataclass(frozen=True)
class Reserva:
    item: str
    inicio: date
    fim: date
    utilizador: str


class ReservaRecusada(Exception):
    """A reserva entra em conflito com outra. Indica a data livre seguinte."""

    def __init__(self, data_livre):
        super().__init__(f"Item ocupado. Livre a partir de {data_livre:%d/%m/%Y}.")
        self.data_livre = data_livre


def sobrepoem(a_inicio, a_fim, b_inicio, b_fim):
    """Dois períodos sobrepõem-se se partilharem pelo menos um dia."""
    return a_inicio <= b_fim and b_inicio <= a_fim


class ServicoReservas:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def reservar(self, item, inicio, fim, utilizador):
        if fim < inicio:
            raise ValueError("A data de fim é anterior à data de início.")
        conflitos = [
            r for r in self.repositorio.reservas_do_item(item)
            if sobrepoem(inicio, fim, r.inicio, r.fim)
        ]
        if conflitos:
            ultimo_dia_ocupado = max(r.fim for r in conflitos)
            raise ReservaRecusada(ultimo_dia_ocupado + timedelta(days=1))
        reserva = Reserva(item, inicio, fim, utilizador)
        self.repositorio.guardar(reserva)
        return reserva
