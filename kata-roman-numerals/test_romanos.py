import pytest
from romanos import para_romano, para_inteiro


@pytest.mark.parametrize("numero, esperado", [
    (1, "I"),
    (2, "II"),
    (3, "III"),
    (4, "IV"),
    (5, "V"),
    (6, "VI"),
    (9, "IX"),
    (10, "X"),
    (1994, "MCMXCIV"),
    (2026, "MMXXVI"),
    (3999, "MMMCMXCIX"),
])
def test_para_romano(numero, esperado):
    assert para_romano(numero) == esperado


@pytest.mark.parametrize("numero", [-1, 0, 4000])
def test_para_romano_fora_do_intervalo(numero):
    with pytest.raises(ValueError, match="O número tem de estar entre 1 e 3999"):
        para_romano(numero)


@pytest.mark.parametrize("numeral, esperado", [
    ("I", 1),
    ("IV", 4),
    ("IX", 9),
    ("XIV", 14),
    ("MCMXCIV", 1994),
    ("MMXXVI", 2026),
    ("MMMCMXCIX", 3999),
])
def test_para_inteiro(numeral, esperado):
    assert para_inteiro(numeral) == esperado


def test_ida_e_volta():
    for n in range(1, 4000):
        assert para_inteiro(para_romano(n)) == n