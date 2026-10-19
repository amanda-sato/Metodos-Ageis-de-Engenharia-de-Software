import pytest
from romanos import para_romano

def test_para_romano():
    assert para_romano(1) == "I"
    # assert para_romano(2) == "II"
    #assert para_romano(3) == "III"
    