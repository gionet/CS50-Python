import pytest
from seasons import Date, get_dates

def test_wrong_format():
    with pytest.raises(ValueError):
        Date.lived_duration("199999/10/10")
        Date.lived_duration("1999/5/2")

def test_out_of_bound():
    with pytest.raises(ValueError):
        Date.lived_duration("3000-2-2")
        Date.lived_duration("2000-13-10")
        Date.lived_duration("3000-12-32")

def test_valid_dates():
    assert Date.lived_duration("2022-11-14") == 365

def test_valid_dates_convert_minutes():
    assert Date.convert_minutes(365) == 525600
    assert Date.convert_minutes(1) == 1440
