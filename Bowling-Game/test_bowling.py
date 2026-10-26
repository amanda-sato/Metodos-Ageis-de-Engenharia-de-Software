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

def test_strike():
    lancamentos = [10, 3, 4] + [0] * 16
    assert pontuacao(lancamentos) == 24

def test_strikes_seguidos():
    lancamentos = [10, 10, 7, 1] + [0] * 14
    assert pontuacao(lancamentos) == 53

def test_spare_na_decima_jogada():
    lancamentos = [0] * 18 + [5, 5, 6]
    assert pontuacao(lancamentos) == 16

