import pytest
from twttr import shorten

def test_vowel_replacement():
    assert shorten('twitter') == 'twttr'
    assert shorten('netflix') == 'ntflx'

def test_capital_vowel():
    assert shorten('twIttEr') == 'twttr'
    assert shorten('nEtflIx') == 'ntflx'

def test_lowercase_vowel():
    assert shorten('garena') == 'grn'

def test_omits_numbers():
    assert shorten('123') == '123'

def test_uppercase():
    assert shorten('VaniLlA') == 'VnLl'

def test_omits_punctuation():
    assert shorten('!AMV3G(A)N') == '!MV3G()N'
