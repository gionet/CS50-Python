import pytest
from numb3rs import validate

def test_numb3rs():
    assert validate("255.255.255.255") == True
    assert validate("1.1.1.1") == True
    assert validate("10.0.1.5") == True

def test_numb3rs_out_of_bound():
    assert validate("273.1.1.1") == False
    assert validate("1.257.1.1") == False
    assert validate("1.2.3.1000") == False
    assert validate("512.512.512.512") == False
    assert validate("2000.1.1.1") == False
    assert validate("20.260.15.35") == False
    assert validate("1.25555.1.1") == False

def test_not_number():
    assert validate("cat") == False

def test_octet_starts_with_zero():
    assert validate("01.1.1.1") == True
    assert validate("10.02.1.1") == True
    assert validate("1.1.06.1") == True
    assert validate("1.1.1.09") == True

