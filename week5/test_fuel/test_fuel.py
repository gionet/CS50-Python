import pytest
from fuel import gauge, convert

def test_error():
    with pytest.raises(ValueError):
        convert('-5/10')
        convert('3/-5')
        convert('4/3')
        convert('-1')
        convert('-4')
        convert('cat')
    with pytest.raises(ZeroDivisionError):
        convert('1/0')
        convert('4/0')
    with pytest.raises(ValueError):
        convert('cat/dog')

def test_empty():
    assert convert('0/4') == 0
    assert convert('1/100') == 1
    assert gauge(1) == 'E'

def test_not_empty_or_full():
    assert convert('2/100') == 2
    assert convert('50/100') == 50
    assert convert('1/4') == 25
    assert gauge(25) == '25%'

def test_full():
    assert convert('99/100') == 99
    assert convert('1/1') == 100
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'

