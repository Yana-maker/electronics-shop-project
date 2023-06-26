"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item():
    item = Item("1", 2, 3)
    return item


def test_init(item):
    assert item.name == "1"
    assert item.price == 2
    assert item.quantity == 3

def test_property(item):

    assert item.name == '1'
    item.name = '3'
    assert item.name == '1'

def test_setter(item):

    item.name = ('fdsfdsfsdfsd')
    assert item.name == 'fdsfdsfsdf'


def test_calculate_total_price(item):

    assert item.calculate_total_price() == 6

def test_apply_discount(item):

    assert item.apply_discount() == 2
    item.pay_rate = 1.5
    assert item.apply_discount() == 3

def test_instantiate_from_csv(item):

    item.instantiate_from_csv()
    assert len(item.all) == 5


def test_string_to_number(item):

    assert item.string_to_number('6') == 6
    assert item.string_to_number('5.5') == 5

def test_repr(item):
    assert repr(item) == "Item('1', 2, 3)"

def test_str(item):
    assert str(item) == '1'