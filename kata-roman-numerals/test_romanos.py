import pytest
from romanos import para_romano

def test_para_romano_1():
    assert para_romano(1) == "I"
    
def test_para_romano_2():
    assert para_romano(2) == "II"

def test_para_romano_3():
    assert para_romano(3) == "III"

def test_para_romano_5():
    assert para_romano(5) == "V"

def test_para_romano_6():
    assert para_romano(6) == "VI"

def test_para_romano_10():
    assert para_romano(10) == "X"

def test_para_romano_4():
    assert para_romano(4) == "IV"

def test_para_romano_9():
    assert para_romano(9) == "IX"

def test_para_romano_1994():    
    assert para_romano(1994) == "MCMXCIV"