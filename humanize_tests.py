import pytest
from humanize import humanize, ERROR_STRING


def test_from_example():
    assert humanize('3+7=10') == 'three plus seven equals ten'


def test_from_example_with_tabs():
    assert humanize('3    +           7   =10') == 'three plus seven equals ten'


def test_incorrect_symbol():
    assert humanize('3/7=s10') == ERROR_STRING


def test_duplicate_operation():
    assert humanize('3 // 7 = 10') == ERROR_STRING


def test_without_number_for_operation():
    assert humanize(' + 7 = 7') == ERROR_STRING


def test_too_large_number():
    assert humanize('1000000000000000') == ERROR_STRING


def test_6():
    assert humanize('6') == 'six'


def test_16():
    assert humanize('16') == 'sixteen'


def test_26():
    assert humanize('26') == 'twenty six'


def test_106():
    assert humanize('106') == 'one hundred six'


def test_116():
    assert humanize('116') == 'one hundred sixteen'


def test_166():
    assert humanize('166') == 'one hundred sixty six'


def test_1006():
    assert humanize('1006') == 'one thousand six'


def test_1016():
    assert humanize('1016') == 'one thousand sixteen'


def test_1060():
    assert humanize('1060') == 'one thousand sixty'


def test_1600():
    assert humanize('1600') == 'one thousand six hundred'


def test_16000():
    assert humanize('16000') == 'sixteen thousand'


def test_166666():
    assert humanize('166666') == 'one hundred sixty six thousand six hundred sixty six'


def test_160millions():
    assert humanize('160000000') == 'one hundred sixty million'


def test_160billions():
    assert humanize('160000000000') == 'one hundred sixty billion'
