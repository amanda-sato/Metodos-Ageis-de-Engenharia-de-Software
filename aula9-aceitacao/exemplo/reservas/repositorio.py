"""Duas formas de guardar reservas, com a mesma interface."""
import sqlite3
from datetime import date

from reservas.servico import Reserva


class RepositorioMemoria:
    """Fake: guarda numa lista. Rápido, serve para testes unitários e de aceitação."""

    def __init__(self):
        self._reservas = []

    def guardar(self, reserva):
        self._reservas.append(reserva)

    def reservas_do_item(self, item):
        return [r for r in self._reservas if r.item == item]


class RepositorioSQLite:
    """Real: guarda num ficheiro SQLite. É este que os testes de integração exercitam."""

    def __init__(self, caminho):
        self._caminho = str(caminho)
        with self._ligar() as bd:
            bd.execute(
                "CREATE TABLE IF NOT EXISTS reservas "
                "(item TEXT, inicio TEXT, fim TEXT, utilizador TEXT)"
            )

    def _ligar(self):
        return sqlite3.connect(self._caminho)

    def guardar(self, reserva):
        with self._ligar() as bd:
            bd.execute(
                "INSERT INTO reservas VALUES (?, ?, ?, ?)",
                (reserva.item, reserva.inicio.isoformat(),
                 reserva.fim.isoformat(), reserva.utilizador),
            )

    def reservas_do_item(self, item):
        with self._ligar() as bd:
            linhas = bd.execute(
                "SELECT item, inicio, fim, utilizador FROM reservas WHERE item = ?",
                (item,),
            ).fetchall()
        return [
            Reserva(i, date.fromisoformat(a), date.fromisoformat(b), u)
            for i, a, b, u in linhas
        ]
