import pytest
from bowling import pontuacao


def test_so_zeros():
    lancamentos = [0] * 20
    assert pontuacao(lancamentos) == 0

def test_jogada_normal():
    lancamentos = [3, 3] + [0] * 18
    assert pontuacao(lancamentos) == 6
