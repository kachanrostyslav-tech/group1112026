import pytest
from utils import calculate_discount, is_even, get_full_name


# calculate_discount: 5 tests
def test_calculate_discount_20_percent():
    assert calculate_discount(100, 20) == pytest.approx(80)

def test_calculate_discount_50_percent():
    assert calculate_discount(80, 50) == pytest.approx(40)

def test_calculate_discount_zero_percent():
    assert calculate_discount(45, 0) == pytest.approx(45)

def test_calculate_discount_zero_price():
    assert calculate_discount(0, 25) == pytest.approx(0)

def test_calculate_discount_another_valid_value():
    assert calculate_discount(59.99, 10) == pytest.approx(53.991)


# is_even: 5 tests
def test_is_even_positive_even_number():
    assert is_even(8) is True

def test_is_even_positive_odd_number():
    assert is_even(7) is False

def test_is_even_negative_even_number():
    assert is_even(-6) is True

def test_is_even_negative_odd_number():
    assert is_even(-5) is False

def test_is_even_zero():
    assert is_even(0) is True


# get_full_name: 5 tests
def test_get_full_name_standard_names():
    assert get_full_name("Ada", "Lovelace") == "Ada Lovelace"

def test_get_full_name_short_names():
    assert get_full_name("Al", "Li") == "Al Li"

def test_get_full_name_long_names():
    assert get_full_name("Alexandria", "Montgomery-Smythe") == "Alexandria Montgomery-Smythe"

def test_get_full_name_single_character_name():
    assert get_full_name("J", "Smith") == "J Smith"

def test_get_full_name_another_valid_case():
    assert get_full_name("Mary", "Jane") == "Mary Jane"
