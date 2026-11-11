from utils.numbers_utils import is_number_bigger_than_10

def test_is_number_bigger_than_10_case_1():
    number = 9
    expected = False
    actual = is_number_bigger_than_10(number)
    assert expected is actual

def test_is_number_bigger_than_10_case_2():
    number = 10
    expected = False
    actual = is_number_bigger_than_10(number)
    assert expected is actual

def test_is_number_bigger_than_10_case_3():
    number = 101
    expected = True
    actual = is_number_bigger_than_10(number)
    assert expected is actual