import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar2 = Jar(5)
    assert jar2.capacity == 5

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(3)
    assert jar.size == 8
    jar.deposit(1)
    assert jar.size == 9

def test_withdraw():
    jar = Jar()
    jar.deposit(6)
    jar.withdraw(4)
    assert jar.size == 2
    jar.deposit(3)
    jar.withdraw(4)
    assert jar.size == 1

def test_error():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(6)
        jar.withdraw(7)

def test_exceed_capacity_error():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(1)
        jar.deposit(12)
