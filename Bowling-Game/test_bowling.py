import pytest
from bowling import pontuacao


def test_so_zeros():
    lancamentos = [0] * 20
    assert pontuacao(lancamentos) == 0

def test_jogada_normal():
    lancamentos = [3, 3] + [0] * 18
    assert pontuacao(lancamentos) == 6

def test_spare():
    lancamentos = [5, 5, 4] + [0] * 17
    assert pontuacao(lancamentos) == 18
