import pytest
from calculator import somar

def test_texto_vazio_devolve_zero():
    assert somar("") == 0


def test_um_numero_devolve_esse_numero():
    assert somar("1") == 1


def test_dois_numeros_devolvem_soma():
    assert somar("1,2") == 3

def test_qualquer_quantidade_de_numeros_devolvem_soma():
    assert somar("1,2,3,4,5") == 15

def test_separador():
    assert somar("//;\n1;2") == 3

def test_numeros_negativos_devolvem_erro():
    with pytest.raises(Exception) as excinfo:
        somar("-1,2,-3")
    assert str(excinfo.value) == "negativos não são permitidos: -1,-3"

def test_numeros_maiores_que_mil_sao_ignorados():
    assert somar("2,1001") == 2

def test_separadores():   
    assert somar("//[***]\n1***2***3") == 6

def test_varios_separadores():
    assert somar("//[*][%]\n1*2%3") == 6