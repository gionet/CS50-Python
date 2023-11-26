import pytest
from um import count

def test_um_plus_special_char():
    assert count("hello, um, world") == 1
    assert count("hello, um, um, um, um, um") == 5
    assert count("Um, thanks, um...") == 2

def test_um_only():
    assert count("um") == 1
    assert count("hello, um") == 1
    assert count("Um, thanks for the album") == 1



