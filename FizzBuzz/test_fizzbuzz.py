from fizzbuzz import fizzbuzz

def test_1_devolve_1():
    assert fizzbuzz(1) == "1"

def test_2_devolve_2():
    assert fizzbuzz(2) == "2"

def test_3_devolve_fizz():
    assert fizzbuzz(3) == "fizz"

def test_4_devolve_buzz():
    assert fizzbuzz(5) == "buzz"

def test_5_devolve_buzz():
    assert fizzbuzz(15) == "FizzBuzz"