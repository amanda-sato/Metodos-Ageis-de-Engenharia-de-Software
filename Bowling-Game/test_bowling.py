import pytest
from bowling import pontuacao


def test_so_zeros():
    lancamentos = [0] * 20
    assert pontuacao(lancamentos) == 0


