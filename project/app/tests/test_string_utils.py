from utils.string_utils import concatenate_strings
def test_concatenate_strings():
    string_1 = "1"
    string_2 = "2"
    expected = "1 2"
    actual = concatenate_strings(string_1, string_2)
    assert expected == actual

def test_concatenate_strings_strip_whitespaces() -> None:
    string_1 = "    1    "
    string_2 = "  2654      "
    expected = "1 2654"
    actual = concatenate_strings(string_1, string_2)
    assert expected == actual

def test_concatenate_strings_3() -> None:
    string_1 = "jk jk   "
    string_2 = ""
    expected = "jk jk"
    actual = concatenate_strings(string_1, string_2)
    assert expected == actual
