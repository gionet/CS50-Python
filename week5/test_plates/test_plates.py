import pytest
from plates import is_valid

def test_starts_two_letter():
    assert is_valid('12AACC') == False
    assert is_valid('CS') == True
    assert is_valid('CS333') == True
    assert is_valid('123') == False

def test_max_6_char():
    assert is_valid('CS11111') == False
    assert is_valid('GGHELLO') == False
    assert is_valid('ACTTTT') == True

def test_number_middle():
    assert is_valid('BB11A') == False
    assert is_valid('BB11') == True
    assert is_valid('BB1') == True
    assert is_valid('AAAA11') == True

def test_zero_placement():
    assert is_valid('BB00') == False
    assert is_valid('ACB01') == False

def test_only_alphanum():
    assert is_valid('AA.') == False
    assert is_valid('AA ') == False
    assert is_valid('A A') == False
    assert is_valid('GAT3?') == False
    assert is_valid('BB33!') == False
    assert is_valid('BBC;') == False



