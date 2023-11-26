import pytest
from bank import value

def test_bank():
    assert value('whats up?') == 100

def test_case_insensitivity():
    assert value('HeLLO') == 0
    assert value('hEyyyy') == 20

def test_not_entire_phrase():
    assert value('Yoow') == 100
